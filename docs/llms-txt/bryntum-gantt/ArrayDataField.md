# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/ArrayDataField.md

# [ArrayDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ArrayDataField)

This field class handles fields that hold an array.

```
class Task extends Model {
    static get fields() {
        return [
            'name',
            // Array field
            { name : 'todo', type : 'array' }
        ];
    }
}
```

A record can be constructed like this:

```
const task = new Task({
    name : 'Task 1',
    todo : [
        { text : 'Something', done : false },
        { text : 'Some other thing', done : true }
    ]
};
```

Or by populating a store:

```
const store = new Store({
    modelClass : Task,
    data : [
        {
            name : 'Task 1',
            todo : [
                { text : 'Something', done : false },
                { text : 'Some other thing', done : true }
            ]
        },
        ...
    ]
});
```

For the field to count as modified, the whole array has to be replaced:

```
// This won't be detected as a modification
task.todo[0].done = true;
// task.isModified === false

// But this will
const todo = task.todo.slice(); // Create a new array with same contents
todo[0].done = true;
task.todo = todo;
// task.isModified === true
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isArrayDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ArrayDataField#property-isArrayDataField)
Identifies an object as an instance of [ArrayDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ArrayDataField) class, or subclass thereof.

[isArrayDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ArrayDataField#property-isArrayDataField-static)
Identifies an object as an instance of [ArrayDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ArrayDataField) class, or subclass thereof.
