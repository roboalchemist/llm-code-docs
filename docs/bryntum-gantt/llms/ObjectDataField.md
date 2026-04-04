# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/ObjectDataField.md

# [ObjectDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ObjectDataField)

This field class handles fields that hold an object.

```
class Person extends Model {
    static fields = [
        'name',
        { name : 'address', type : 'object' }
    ];
}
```

For the field to count as modified, the whole object has to be replaced:

```
person.address = { ...address };
```

Or, sub properties of the object has to be modified using calls to `set()`:

```
person.set('address.street', 'Main Street');
```

Note that if any property of the nested object requires conversion after load, you have to define that property as a field:

```
class Order extends Model {
    static fields = [
        'title',
        { name : 'details', type : 'object' },
        { name : 'details.date', type : 'date' }
    ];
}

const order = new Order({
   title   : 'Order 1',
   details : {
     customer : 'Bill',
     // Definition above required for this to be converted to a date
     date     : '2020-01-01'
   }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isObjectDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ObjectDataField#property-isObjectDataField)
Identifies an object as an instance of [ObjectDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ObjectDataField) class, or subclass thereof.

[isObjectDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ObjectDataField#property-isObjectDataField-static)
Identifies an object as an instance of [ObjectDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ObjectDataField) class, or subclass thereof.
