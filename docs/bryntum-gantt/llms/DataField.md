# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/DataField.md

# [DataField](https://bryntum.com/docs/gantt/api/Core/data/field/DataField)

This is the base class for Model field classes. A field class defines how to handle the data for a particular type of field. Many of these behaviors can be configured on individual field instances.

While defining `fields` on [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) in TypeScript, data fields should be of type `ModelFieldConfig` instead of `DataField`, because it is a union type that gives completion based on specified type.

```
class Person extends Model {
     static name: string = 'Person'

     static fields: ModelFieldConfig[] = [
         { name: 'address', type: 'string' },
         { name: 'contact', type: 'int' }
     ]
}

```

Calculated fields
-----------------

A field value can also be calculated using the other data fields, using the [calculate](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-calculate) config.

```
const store = new Store({
    fields : [
        { name : 'revenue', type : 'number' },
        { name : 'tax', type : 'number' },
        { name : 'net', calculate : record => record.revenue * (1 - (record.tax / 100)) },
    ],
    data : [
        { id : 1, revenue : 100, tax : 30 }
    ]
});

const record = store.getById(1).net; // 70
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[name](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-name)
The name of the field.

If the name contains a dot (`.`), it is assumed to be a nested field, and the `complexMapping` config is automatically set to `true`. This means that the field will point to nested data (path separated by dots in the field name). Configure it as `false` to allow data field names that actually contain dots. See [complexMapping](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-complexMapping) for more information.

[label](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-label)
The label text for a form item generated for this field. This is also used to create a column header for a [column](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-column) for this field.

If no label is specified, the value yielded by this property is a prettified version of the field name created using [separate](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-separate-static).

[column](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-column)
A column config object for a column to display this field in a grid. For simple, atomic data types, such as `date`, `string`, `boolean`, `number` and `integer`, this is optional and the appropriate column type can be inferred.

This also provides default values for column configuration if a configured column definition for a grid lacks a property.

For complex fields, such as identifiers which link to other records, a more capable column type may be specified, for example a `type : 'number'` field may be configured with

```
column : 'percent'
```

or

```
column : {
    type : 'percent',
    width : 100
}
```

if it represents a percentage value and needs appropriate rendering and editing.

[editor](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-editor)
A config object for a widget to edit this field in a form. For simple, atomic data types, such as `date`, `string`, `boolean`, `number` and `integer`, this is optional and the appropriate input widget type can be inferred.

For complex fields, such as identifiers which link to other records, a more capable widget may be specified.

[compare](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-compare)
A function that compares two values and returns a value < 0 if the first is less than the second, or 0 if the values are equal, or a value > 0 if the first is greater than the second.

[compareItems](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-compareItems)
A function that compares two objects or records using the `compare` function on the properties of each object based on the `name` of this field.

[dataSource](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-dataSource)
The property in a record's data object that contains the field's value. Defaults to the field's `name`.

[defaultValue](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-defaultValue)
The default value to assign to this field in a record if no value is provided.

[alwaysWrite](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-alwaysWrite)
Setting to `true` will ensure this field is included in any update/insert request payload when a Store / Project / CrudManager performs a request.

[nullable](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-nullable)
Setting to `false` indicates that `null` is not a valid value.

[nullText](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-nullText)
The value to return from [print](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#function-print) for a `null` or `undefined` value.

[nullValue](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-nullValue)
The value to replace `null` when the field is not `nullable`.

[persist](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-persist)
Set to `false` to exclude this field when saving records to a server.

[readOnly](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-readOnly)
Set to `true` for the field's set accessor to ignore attempts to set this field.

[internal](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-internal)
By default, defined [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) fields may be used to create a grid column suitable for displaying that field in a grid cell. Some fields may not be suitable for features which automatically generate columns for view. These fields are created using `internal : true`. Some examples are the `expanded` and `rowHeight` fields which are used internally.

[calculated](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-calculated)
Set to `true` to indicate this field is calculated and cannot be edited via UI

[calculate](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-calculate)
Lets you define a function to calculate the value of this field based on other record fields. The Model will then try to auto-detect the dependencies used in the function. The calculate function can also return a `Promise`, meaning you can fetch its value from a remote/async source.

```
const store = new Store({
    fields : [
        {
             name : 'revenue',
             type : 'number'
        },
        {
             name : 'tax',
             type : 'number'
        },
        {
             name : 'net',
             calculate : record => record.revenue * (1 - (record.tax / 100)),
        }
    ],
    data : [
        { id : 1, revenue : 100, tax : 30 }
    ]
});

const record = store.getById(1).net; // 70
```

You can also pass an object with a `dependsOn` array of the dependent fields, along with the calculate `fn`:

```
const store = new Store({
    fields : [
        {
             name : 'revenue',
             type : 'number'
        },
        {
             name : 'tax',
             type : 'number'
        },
        {
             name : 'net',
             calculate : {
                 fn        : record => record.revenue * (1 - (record.tax / 100)),
                 dependsOn : ['revenue', 'tax']
             }
        }
    ],
    data : [
        { id : 1, revenue : 100, tax : 30 }
    ]
});

const record = store.getById(1).net; // 70
```

[bypassEqualityOnSyncDataset](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-bypassEqualityOnSyncDataset)
When this flag is enabled, this field will skip the equality check when store is syncing the new dataset (see [syncDataOnLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-syncDataOnLoad) config). This means, that even if the new value in new dataset is the same as old, it will still be applied to the model. It is useful in certain edge case scenarios, when the update of the field does not preserve extra context information, which should be provided by other fields.

[complexMapping](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-complexMapping)
Indicates that this field points to nested data (path separated by dots in the field name). Normally this is set automatically when a field's [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) or [dataSource](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-dataSource) contains a dot (`.`). Configure it as `false` to allow data field names that actually contain dots.

```
class MyModel extends Model {
   static fields = [
       // complexMapping automatically set to true,
       // `name.first` will point to { name : { first : "value" } }
       { name : 'name.first', type : 'string' },

       // complexMapping automatically set to true,
       // `last` will point to { name : { last : "value" } }
       { name : 'last', type : 'string', dataSource : 'name.last' },

       // complexMapping set to false,
       // `not.nested.name` will point to { "not.nested.name" : "value" }
       { name : 'not.nested.name', complexMapping : false }
   ];
}
```

[formulaProviders](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-formulaProviders)
An object which names formula prefixes for use when editing this field.

Each entry is keyed by a formula prefix, and each value is how to instantiate and configure a [FormulaProvider](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider) when that prefix is used in the typed vale, eg: `=XXX(`

If the configured value contains a `type` property, that is used to determine a registered formula provider subclass to instantiate.

```
fields : [{
    name             : 'review',
    formulaProviders : {
       AI : {
         type : 'remote',
         url  : 'https://my-ai-service.com'
       },
       SUM : {
          type : 'sum'
       }
    }
}]
```

Formula providers may be added to dynamically:

```
// Enable registered MYFormula class to be used as a formula provider in the Grid
grid.store.modelClass.fieldMap.review.formulaProviders.MY = { ... };
```

[description](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#config-description)
A description used by the AI features to explain the field to the AI agent

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDataField](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#property-isDataField)
Identifies an object as an instance of [DataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField) class, or subclass thereof.

[isDataField](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#property-isDataField-static)
Identifies an object as an instance of [DataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField) class, or subclass thereof.

[definedBy](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#property-definedBy)
The class that first defined this field. Derived classes that override a field do not change this property.

[owner](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#property-owner)
The class that most specifically defined this field. Derived classes that override a field set this property to themselves.

## Functions

Functions are methods available for calling on the class

[convert](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-convert)
This method transforms a data value into the desired form for storage in the record's data object.

```
export default class Task extends TaskModel {
   static get fields() {
       return [
           {
               name    : 'status',
               convert : (value, data) => {
                   if (value >= 100) {
                       return 'done';
                   }
                   else if (value > 0) {
                       return 'started';
                   }
               }
           }
       ];
   }
}
```

[serialize](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-serialize)
This method transforms a data value into the desired form for transmitting to a server.

[set](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-set)
This optional method is called when setting a data value on a record.

[init](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-init)
This optional method is called when a record using this field is created.

[defineAccessor](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-defineAccessor)
Create getter and setter functions for the specified field name under the specified key.

[isEqual](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-isEqual)
Compares two values for this field and returns `true` if they are equal, and `false` if not.

[print](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-print)
Returns the given field value as a `String`. If `value` is `null` or `undefined`, the value specified by [nullText](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-nullText) is returned.

[printValue](https://bryntum.com/docs/gantt/api/Core/data/field/DataField#function-printValue)
Returns the given, non-null field value as a `String`.
