# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/Model.md

# [Model](https://bryntum.com/docs/gantt/api/Core/data/Model)

A Model is the definition of a record which can be added to (or loaded into) a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store). It defines which fields the data contains and exposes an interface to access and manipulate that data. The Model data is populated through simple a JSON object.

By default, a Model stores a shallow copy of its raw json, but for records in stores configured with `useRawData: true` it stores the supplied json object as is.

Defining fields
---------------

A Model can either define its fields explicitly (see [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields-static)) or have them created from its data (see [autoExposeFields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-autoExposeFields-static)). This snippet shows a model with 4 fields defined explicitly:

```
class Person extends Model {
    static fields = [
        'name',
        { name : 'birthday', type : 'date', format : 'YYYY-MM-DD' },
        { name : 'shoeSize', type : 'number', defaultValue : 11 },
        { name : 'age', readOnly : true }
    ]
}
```

The first field (name) has an unspecified type, which means the field's value is held as received with no conversion applied. The second field (birthday) is defined to be a date, which will make the model parse any supplied value into an actual date. The parsing is handled by [DateHelper.parse()](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parse-static) using the specified `format`, or if no format is specified using [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static).

While defining `fields` on [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) in TypeScript, data fields should be of type `ModelFieldConfig` instead of `DataField`, because it is a union type that gives completion based on specified type.

```
class Person extends Model {
    static fields: ModelFieldConfig[] = [
        'name',
        { name : 'birthday', type : 'date', format : 'YYYY-MM-DD' },
        { name : 'shoeSize', type : 'number', defaultValue : 11 },
        { name : 'age', readOnly : true }
    ]
}
```

The set of standard field types is as follows:

* [`array`](https://bryntum.com/docs/gantt/api/#Core/data/field/ArrayDataField)
* [`boolean`](https://bryntum.com/docs/gantt/api/#Core/data/field/BooleanDataField)
* [`date`](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField)
* [`integer`](https://bryntum.com/docs/gantt/api/#Core/data/field/IntegerDataField)
* [`object`](https://bryntum.com/docs/gantt/api/#Core/data/field/ObjectDataField)
* [`number`](https://bryntum.com/docs/gantt/api/#Core/data/field/NumberDataField)
* [`store`](https://bryntum.com/docs/gantt/api/#Core/data/field/StoreDataField)
* [`string`](https://bryntum.com/docs/gantt/api/#Core/data/field/StringDataField)

You can also set a `defaultValue` that will be used if the data does not contain a value for the field:

```
{ name : 'shoeSize', type : 'number', defaultValue : 11 }
```

Defining a field with a `name` containing a `.` will by default point to a nested object in the data. If you have a data property that actually contains a `.` in the name, also configure `complexMapping : false` on the field:

```
class Organization extends Model {
    static fields = [
        // Points to { "org" : { "name" : "..." } } in the data
        { name : 'org.name' },
        // Points to { "org.address" : "..." } in the data
        { name : 'org.address', complexMapping : false }
    ]
}
```

Creating a record
-----------------

To create a record from a Model, supply data to its constructor:

```
const guy = new Person({
    id       : 1,
    name     : 'Dude',
    birthday : '2014-09-01'
});
```

If no id is specified, a temporary id based on a UUID will be generated. This id is not meant to be serialized, it should instead be replaced by the backend with a proper id from the underlying database (or similar).

Please avoid using reserved names for your fields (such as `parent`, `children` and others that are used as Model properties) to avoid possible data collisions and bugs.

When adding data to a Store, you do normally not need to create records manually. The store does that for you when you add a data object to it

Calculated fields
-----------------

A field value can also be calculated using the other data fields, using the [calculate](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-calculate) config.

```
const store = new Store({
    fields : [
        { name : 'revenue', type : 'number' },
        { name : 'tax', type : 'number' },
        { name : 'net', calculate : record => record.revenue * (1 - (record.tax / 100)) }
    ],
    data : [
        { id : 1, revenue : 100, tax : 30 }
    ]
});

const record = store.getById(1).net; // 70
```

Nested fields
-------------

Model supports mapping fields to nested data structures using dot `.` separated paths as the `dataSource`. For example given this JSON object:

```
{
    name : 'Borje Salming',
    team : {
        name   : 'Toronto Maple Leafs',
        league : 'NHL'
    }
}
```

A field can be mapped to the nested team name by using `dataSource : 'team.name'`:

```
class Player extends Model {
    static fields = [
        'name',
        // Field mapped to a property on a nested object
        { name : 'teamName', dataSource : 'team.name' }
    ];
}
```

Usage:

```
const player = new Player(json);

console.log(player.teamName); // > Toronto Maple Leafs
player.teamName = 'Minnesota Wild'; // Updates name property of the team object
```

Alternatively, you can define the top level of the nested object as a field of type `object`:

```
class Person extends Model {
    static fields = [
        'name',
        // Nested object
        { name : 'address', type : 'object' }
    ];
}
```

You can then access properties of the nested object using dot notation with the [get](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-get) function:

```
const person = new Person({
   name    : 'Borje Salming',
   address : {
       city : 'Toronto'
   }
});

person.get('address.city'); // > Toronto
```

### Updating a nested object

Note that directly altering a property of the nested object won't register as an update of the record, record does not track changes deeply. If nested fields (as described above) is not enough for your usecase you can map a field directly to the nested object and then assign a shallow copy of it to the record on changes:

```
class Player extends Model {
    static get fields() {
        return [
            ...,
            // Field mapped directly to the nested object
            { name : 'team', type : 'object' }
        ]
    }
}

// "External object" to nest
const team = {
    name   : 'Brynas',
    league : 'SHL'
}

const player = new Player({
    name : 'Borje Salming',
    team
});

// This will not flag player as dirty
team.league = 'CHL';

// Instead you have to reassign the mapped field
player.team = { ...player.team };
```

You can also use the [set](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) function to update a property of the nested object:

```
// This will flag player as dirty
player.set('team.name', 'BIF');
```

Arrays of atomic types
----------------------

When a field holds an array of atomic types (strings, numbers etc.) we recommend using the [`array`](https://bryntum.com/docs/gantt/api/#Core/data/field/ArrayDataField) type for the field:

```
class GroceryList extends Model {
    static get fields() {
        return [
            'name',
            { name : 'items', type : 'array' }
        ];
    }
}

const list = new GroceryList({
   name  : 'My list',
   items : ['Milk', 'Bread', 'Eggs']
});
```

Modifying items in the array will not flag the field as updated, since the array itself does not change. For it to register a change, you must assign it a new array (could be a copy of the old one). For more info, see [ArrayDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ArrayDataField)

Arrays of objects
-----------------

When a field holds an array of objects, we recommend using the [`store`](https://bryntum.com/docs/gantt/api/#Core/data/field/StoreDataField) type for the field:

```
class GroceryList extends Model {
    static fields = [
        'name',
        { name : 'items', type : 'store', storeClass : Store }
    ]
}

const list = new GroceryList({
   name  : 'My list',
   items : [
       { name : 'Milk', quantity : 1 },
       { name : 'Bread', quantity : 2 },
       { name : 'Eggs', quantity : 12 }
   ]
});
```

The `items` field on the `list` above will be a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) instance (because we passed that as `storeClass`), which can be used to manipulate the items in the list. Doing so will flag the `list` as modified. For more info, see [StoreDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/StoreDataField).

Persisting fields
-----------------

By default, all fields are persisted. If you don't want particular field to get saved to the server, configure it with `persist: false`. In this case field will not be among changes which are sent by [store.commit()](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#function-commit), otherwise its behavior doesn't change.

```
class Person extends Model {
    static get fields() {
        return [
            'name',
            { name : 'age', persist : false }
        ];
    }
}
```

The `id` field
--------------

By default Model expects its id field to be stored in a data source named "id". The data source for the id field can be customized by setting [dataSource](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-dataSource) on the id field object configuration.

```
class Person extends Model {
    static fields = [
        { name : 'id', dataSource: 'personId'},
        'name',
        { name : 'age', persist : false },
        { name : 'birthday', type : 'date' }
     ];
}

let girl = new Person({
    personId : 2,
    name     : 'Lady',
    birthday : '2011-11-05'
});
```

Also, it is possible to change the id field data source by setting [idField](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-idField-static):

```
class Person extends Model {
    // Id drawn from 'id' property by default; use custom field here
    static idField = 'personId';

    static fields = [
        'name',
        { name : 'age', persist : false },
        { name : 'birthday', type : 'date' }
    ];
}
```

Getting and setting values
--------------------------

Fields are used to generate getters and setters on the records. Use them to access or modify values (they are reactive):

```
console.log(guy.name);
girl.birthday = new Date(2011,10,6);
```

NOTE: In an application with multiple different models you should subclass Model, since the prototype is decorated with getters and setters. Otherwise, you might get unforeseen collisions.

Field data mapping
------------------

By default, fields are mapped to data using their name. If you for example have a "name" field it expects data to be `{ name: 'Some name' }`. If you need to map it to some other property, specify `dataSource` in your field definition:

```
class Person extends Model {
    static fields = [
        { name : 'name', dataSource : 'TheName' }
    ];
}

// This is now OK:
let dude = new Person({ TheName : 'Manfred' });
console.log(dude.name); // --> Manfred
```

NOTE: Do not modify fields using `dataSource`, as it is intended only for reading and writing from the raw data object. Fields should be modified using `name` as it is the public interface.

Field inheritance
-----------------

Fields declared in a derived model class are added to those from its superclass. If a field declared by a derived class has also been declared by its super class, the field properties of the super class are merged with those of the derived class.

For example:

```
 class Person extends Model {
     static fields = [
         'name',
         { name : 'birthday', type : 'date', format : 'YYYY-MM-DD' }
     ];
 }

 class User extends Person {
     static fields = [
         { name : 'birthday', dataSource : 'dob' },
         { name : 'lastLogin', type : 'date' }
     ];
 }
```

In the above, the `Person` model declares the `birthday` field as a `date` with a specified `format`. The `User` model extends `Person` and also declares the `birthday` field. This redeclared field only specifies `dataSource`, so all the other fields are preserved from `Person`. The `User` model also adds a `lastLogin` field.

Note that later accessing `Person.fields` will refer to the block of two fields defined above (birthday & lastLogin), not to all fields available (name, birthday, lastLogin). To access all fields, use [allFields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-allFields-static) on the Model class instead, or the [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields) property on a record (instance).

The `User` from above could have been declared like so to achieve the same `fields`:

```
 class User extends Model {
     static fields = [
         'name',
         { name : 'birthday', type : 'date', format : 'YYYY-MM-DD', dataSource : 'dob' },
         { name : 'lastLogin', type : 'date' }
     ];
 }
```

Override default values
-----------------------

In case you need to define default value for a specific field, or override an existing default value, you can define a new or re-define an existing field definition in [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields-static) static getter:

```
class Person extends Model {
    static fields = [
        { name : 'username', defaultValue : 'New person' },
        { name : 'birthdate', type : 'date' }
    ];
}

class Bot extends Person {
    static fields = [
        { name : 'username', defaultValue : 'Bot' } // default value of 'username' field is overridden
    ];
}
```

Read-only records
-----------------

Model has a default field called [readOnly](https://bryntum.com/docs/gantt/api/#Core/data/Model#field-readOnly), which is used to make the record read-only in the UI while still allowing programmatic changes to it. Setting it to `true` will prevent it from being edited by the built-in editing features (cell editing in Grid, event dragging in Scheduler, task editor in Gantt etc.). Please note that it is not made read-only on the data level, the record can still be manipulated by application code.

```
// Prevent record from being manipulated by the user
record.readOnly = true;

// Programmatic manipulation is still allowed
record.remove();
```

Tree API
--------

This class mixes in the [TreeNode](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode) mixin which provides an API for tree related functionality (only relevant if your store is configured to be a [tree](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-tree)).

## Fields

Fields belong to a Model class and define the Model data structure

[readOnly](https://bryntum.com/docs/gantt/api/Core/data/Model#field-readOnly)
Flag the record as read-only on the UI level, preventing the end user from manipulating it using editing features such as cell editing and event dragging.

Does not prevent altering the record programmatically, it can still be manipulated by application code.

For more info, see the "Read-only records" section above.

[expanded](https://bryntum.com/docs/gantt/api/Core/data/Model#field-expanded)
Start expanded or not (only valid for tree data)

[id](https://bryntum.com/docs/gantt/api/Core/data/Model#field-id)
Unique identifier for the record. Might be mapped to another dataSource using idField, but always exposed as record.id. Will get a generated value if none is specified in records data.

Note that generated ids are meant to be temporary (phantom ids), they should not be serialized but instead replaced by the backend on commit

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isModel](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isModel)
Identifies an object as an instance of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) class, or subclass thereof.

[isModel](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isModel-static)
Identifies an object as an instance of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) class, or subclass thereof.

[$name](https://bryntum.com/docs/gantt/api/Core/data/Model#property-$name-static)
Class name getter. Used when original ES6 class name is minified or mangled during production build. Should be overridden in each class which extends Model or it descendants.

```
class MyNewClass extends Model {
    static $name = 'MyNewClass';
}
```

[fields](https://bryntum.com/docs/gantt/api/Core/data/Model#property-fields-static)
Array of defined fields for this model class. Subclasses add new fields by implementing this static getter:

```
// Model defining two fields
class Person extends Model {
    static get fields() {
        return [
            { name : 'username', defaultValue : 'New person' },
            { name : 'birthdate', type : 'date' }
        ];
    }
}

// Subclass overriding one of the fields
class Bot extends Person {
    static get fields() {
        return [
            // Default value of 'username' field is overridden, any other setting from the parents
            // definition is preserved
            { name : 'username', defaultValue : 'Bot' }
        ];
    }
}
```

Fields in a subclass are merged with those from the parent class, making it easy to override mappings, formats etc.

Note that later accessing `Bot.fields` will refer to the block with the redefinition of the `username` field seen above, not to all fields available (username, birthdate). To access all fields, use either [allFields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-allFields-static) on the Model class, or the [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields) property on a record.

[relations](https://bryntum.com/docs/gantt/api/Core/data/Model#property-relations-static)
Override in a subclass of Model to define relations to records in other stores.

Always defined on the "one" side, not the "many" side.

Expects an object where keys are relation names and values are [relation configs](https://bryntum.com/docs/gantt/api/#Core/data/Model#typedef-RelationConfig).

This snippet will define a relation called `team`, allowing access to the foreign record via `player.team`. It will point to a record in the `teamStore` (must be available as `record.firstStore.teamStore)` with an id matching the players `teamId` field. The team record in turn, will have a field called `players` which is a collection of all players in the team.

```
class Player extends Model {
    static relations = {
        // Define a relation between a player and a team
        team : {
            foreignKey            : 'teamId',
            foreignStore          : 'teamStore',
            relatedCollectionName : 'players'
        }
    }
}

const teamStore = new Store({
    data : [
        { id : 1, name : 'Brynas' },
        { id : 2, name : 'Leksand' }
    ]
});

const playerStore = new Store({
    modelClass : Player,
    // Matches foreignStore, allowing records of playerStore to find the related store
    teamStore,
    data       : [
        // teamId is specified as foreignKey, will be used to match the team
        { id : 1, name : 'Nicklas Backstrom', teamId : 1  },
        { id : 2, name : 'Elias Lindholm',   teamId : 1  },
        { id : 3, name : 'Filip Forsberg',  teamId : 2  }
    ],
}

playerStore.first.team.name // > Brynas
playerStore.last.team.name // > Leksand
teamStore.first.players // > [nick, elias]
teamStore.last.players // > [filip]
```

To access the related record from the many side, use dot notation for the field name. For example in a Grid column:

```
const grid = new Grid({
   store : playerStore,
   columns : [
       { field : 'name', text : 'Name' },
       { field : 'team.name', text : 'Team' }
   ]
});
```

[defaults](https://bryntum.com/docs/gantt/api/Core/data/Model#property-defaults-static)
Template static getter which is supposed to be overridden to define default field values for the Model class. Overrides `defaultValue` config specified by the [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields-static) getter. Returns a named object where key is a field name and value is a default value for the field.

NOTE: This is a legacy way of defining default values, we recommend using [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields-static) moving forward.

```
class Person extends Model {
    static get fields() {
        return [
            { name : 'username', defaultValue : 'New person' }
        ];
    }
}

class Bot extends Person {
    static get defaults() {
        return {
            username : 'Bot' // default value of 'username' field is overridden
        };
    }
}
```

[idField](https://bryntum.com/docs/gantt/api/Core/data/Model#property-idField-static)
The data source for the id field which provides the ID of instances of this Model.

[childrenField](https://bryntum.com/docs/gantt/api/Core/data/Model#property-childrenField-static)
The name of the data field which holds children of this Model when used in a tree structure

```
MyModel.childrenField = 'kids';
const parent = new MyModel({
    name : 'Dad',
    kids : [
        { name : 'Daughter' },
        { name : 'Son' }
    ]
});
```

[indexPath](https://bryntum.com/docs/gantt/api/Core/data/Model#property-indexPath)
Returns index path to this node. This is the index of each node in the node path starting from the topmost parent. (only relevant when its part of a tree store).

[generatedParent](https://bryntum.com/docs/gantt/api/Core/data/Model#property-generatedParent)
Reports `true` when the record is a parent record generated by the TreeGroup feature.

Only valid for stores used with [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature enabled.

[key](https://bryntum.com/docs/gantt/api/Core/data/Model#property-key)
Holds the value that a generated group parent represents when using the TreeGroup feature.

Only valid for stores used with [TreeGroup](https://bryntum.com/docs/gantt/api/#Grid/feature/TreeGroup) feature.

[isCreating](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isCreating)
Set this property to `true` when adding a record on a conditional basis, that is, it is yet to be confirmed as an addition.

When this is set, the [isPersistable](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-isPersistable) value of the record is **false**, and upon being added to a Store it will _not_ be eligible to be synced with the server as an added record.

Subsequently, _clearing_ this property means this record will become persistable and eligible for syncing as an added record.

[allFields](https://bryntum.com/docs/gantt/api/Core/data/Model#property-allFields-static)
An array containing all the _defined_ fields for this Model class. This will include all superclass's defined fields.

[allFields](https://bryntum.com/docs/gantt/api/Core/data/Model#property-allFields)
Same as [allFields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-allFields-static).

[fieldMap](https://bryntum.com/docs/gantt/api/Core/data/Model#property-fieldMap-static)
An object containing all the _defined_ fields for this Model class. This will include all superclass's defined fields through its prototype chain. So be aware that `Object.keys` and `Object.entries` will only access this class's defined fields.

[fieldMap](https://bryntum.com/docs/gantt/api/Core/data/Model#property-fieldMap)
Same as [fieldMap](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fieldMap-static).

[autoExposeFields](https://bryntum.com/docs/gantt/api/Core/data/Model#property-autoExposeFields-static)
Flag checked from Store when loading data that determines if fields found in first records should be exposed in same way as predefined fields.

Note that we for all but the most basic use cases recommend explicitly defining the fields. Having them auto exposed can lead to unexpected behavior, if the first record is not complete (fields missing, null etc).

[fields](https://bryntum.com/docs/gantt/api/Core/data/Model#property-fields)
Convenience getter to get field definitions from class.

[fieldNames](https://bryntum.com/docs/gantt/api/Core/data/Model#property-fieldNames)
Get the names of all properties in the data object.

Note that this is not the same as the fields defined for the model, in most cases you probably want to use [fields](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-fields) instead.

[classDisplayName](https://bryntum.com/docs/gantt/api/Core/data/Model#property-classDisplayName)
Returns the string value for display purposes of an instance of this Model class. Needs to be overridden in subclasses.

[isPersistable](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isPersistable)
This yields `true` if this record is eligible for syncing with the server. It can yield `false` if the record is in the middle of a [batched update](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-isBatchUpdating), or if it is a [tentative record](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-isCreating) yet to be confirmed as a new addition.

[isModified](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isModified)
True if this model has any uncommitted changes.

[modifications](https://bryntum.com/docs/gantt/api/Core/data/Model#property-modifications)
Get a map of the modified fields in form of an object. The field _names_ are used as the property names in the returned object, and the property values are the latest field values.

The `id` field is always included.

[modificationData](https://bryntum.com/docs/gantt/api/Core/data/Model#property-modificationData)
Get a map of the modified fields in form of an object. The field´s [dataSource](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-dataSource) is used as the property name in the returned object. The record´s id is always included.

[rawModificationData](https://bryntum.com/docs/gantt/api/Core/data/Model#property-rawModificationData)
Returns a map of the modified persistable fields

[modificationDataToWrite](https://bryntum.com/docs/gantt/api/Core/data/Model#property-modificationDataToWrite)
Get a map of the modified data fields along with any [alwaysWrite](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-alwaysWrite) fields, in form of an object. The field´s _dataSource_ is used as the property name in the returned object. Used internally by AjaxStore / CrudManager when sending updates.

[persistableData](https://bryntum.com/docs/gantt/api/Core/data/Model#property-persistableData)
Returns data for **all** [persistable](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-persist) fields in form of an object, using dataSource if present.

[isCommitting](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isCommitting)
True if this models changes are currently being committed.

[internalId](https://bryntum.com/docs/gantt/api/Core/data/Model#property-internalId)
Gets the records internalId. It is assigned during creation, guaranteed to be globally unique among models.

[isPhantom](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isPhantom)
Returns true if the record is new and has not been persisted (and received a proper id).

[hasGeneratedId](https://bryntum.com/docs/gantt/api/Core/data/Model#property-hasGeneratedId)
Checks if record has a generated id.

New records are assigned a generated id based on a UUID (starting with `_generated`), which is intended to be temporary and should be replaced by the backend on commit.

[json](https://bryntum.com/docs/gantt/api/Core/data/Model#property-json)
Get the records data as a json string.

```
const record = new Model({
    title    : 'Hello',
    children : [
        ...
    ]
});

const jsonString = record.json;

//jsonString:
'{"title":"Hello","children":[...]}'
```

[isBatchUpdating](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isBatchUpdating)
True if this Model is currently batching its changes.

[copyOf](https://bryntum.com/docs/gantt/api/Core/data/Model#property-copyOf)
For copied records, this property links to the original model instance from which it was copied.

[isValid](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isValid)
Check if record has valid data. Default implementation returns true, override in your model to do actual validation.

[firstStore](https://bryntum.com/docs/gantt/api/Core/data/Model#property-firstStore)
Get the first store that this model is assigned to.

[isRemoved](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isRemoved)
Returns true if this record is not part of any store.

[groupChildren](https://bryntum.com/docs/gantt/api/Core/data/Model#property-groupChildren)
When called on a group header row returns list of records in that group. Returns `undefined` otherwise.

[isGroupHeader](https://bryntum.com/docs/gantt/api/Core/data/Model#property-isGroupHeader)
Returns true for a group header record

## Functions

Functions are methods available for calling on the class

[constructor](https://bryntum.com/docs/gantt/api/Core/data/Model#function-constructor)
Constructs a new record from the supplied data config.

[equals](https://bryntum.com/docs/gantt/api/Core/data/Model#function-equals)
Compares this Model instance to the passed instance. If they are of the same type, and all fields (except, obviously, `id`) are equal, this returns `true`.

[processData](https://bryntum.com/docs/gantt/api/Core/data/Model#function-processData-static)
Processes raw data, converting values and setting defaults.

[exposeProperties](https://bryntum.com/docs/gantt/api/Core/data/Model#function-exposeProperties-static)
Makes getters and setters for fields (from definitions and data). Called once when class is defined and once when data is loaded first time.

[addField](https://bryntum.com/docs/gantt/api/Core/data/Model#function-addField-static)
Add a field definition in addition to those predefined in `fields`.

[removeField](https://bryntum.com/docs/gantt/api/Core/data/Model#function-removeField-static)
Remove a field definition by name.

[exposeRelations](https://bryntum.com/docs/gantt/api/Core/data/Model#function-exposeRelations-static)
Makes getters and setters for related records. Populates a Model#relation array with the relations, to allow it to be modified later when assigning stores.

[fieldSorter](https://bryntum.com/docs/gantt/api/Core/data/Model#function-fieldSorter-static)
This function forces correct field order. Correct order is parentId before id. If we process id field before parentId, idMap won't be updated and changing parent node will lead to duplicated records in storage

[getFieldDefinition](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getFieldDefinition)
Convenience function to get the definition for a field from class.

[getFieldDefinition](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getFieldDefinition-static)
Get the definition for a field by name.

[getFieldDataSource](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getFieldDataSource-static)
Returns dataSource configuration for a given field name

[getDataSource](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getDataSource)
Get the data source used by specified field. Returns the fieldName if no data source specified.

[processField](https://bryntum.com/docs/gantt/api/Core/data/Model#function-processField-static)
Processes input to a field, converting to expected type.

[initRelations](https://bryntum.com/docs/gantt/api/Core/data/Model#function-initRelations)
Initializes model relations. Called from store when adding a record.

[initRelation](https://bryntum.com/docs/gantt/api/Core/data/Model#function-initRelation)
Initializes/updates a single relation.

[getRelationConfig](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getRelationConfig)
Get a relation config by name, from the first store.

[get](https://bryntum.com/docs/gantt/api/Core/data/Model#function-get)
Get value for specified field name. You can also use the generated getters if loading through a Store. If model is currently in batch operation this will return updated batch values which are not applied to Model until endBatch() is called.

[setData](https://bryntum.com/docs/gantt/api/Core/data/Model#function-setData)
Internal function used to update a records underlying data block (record.data) while still respecting field mappings. Needed in cases where a field needs setting without triggering any associated behaviour and it has a dataSource with a different name.

For example:

```
// startDate mapped to data.beginDate
{ name : 'startDate', dataSource : 'beginDate' }

// Some parts of our code needs to update the data block without triggering any of the behaviour associated with
// calling set. This would then not update "beginDate":
record.data.startDate = xx;

// But this would
record.setData('startDate', xx);
```

[getData](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getData)
Returns raw data from the encapsulated data object for the passed field name

[syncId](https://bryntum.com/docs/gantt/api/Core/data/Model#function-syncId)
Silently updates record's id with no flagging the property as modified. Triggers onModelChange event for changed id.

[set](https://bryntum.com/docs/gantt/api/Core/data/Model#function-set)
Set value for the specified field. You can also use the generated setters if loading through a Store.

Setting a single field, supplying name and value:

```
record.set('name', 'Clark');
```

Setting multiple fields, supplying an object:

```
record.set({
    name : 'Clark',
    city : 'Metropolis'
});
```

NOTE: Do not modify fields using `dataSource`, as it is intended only for reading and writing from the raw data object. Fields should be modified using `name` as it is the public interface.

[refreshCalculatedField](https://bryntum.com/docs/gantt/api/Core/data/Model#function-refreshCalculatedField)
Recalculates the value of a calculated field

[isFieldModified](https://bryntum.com/docs/gantt/api/Core/data/Model#function-isFieldModified)
Returns `true` if this model has uncommitted changes for the provided field.

[getUnmodified](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getUnmodified)
Returns the unmodified value of the field, as in the value it had after the last commit. If the field has not been modified, the current value is returned.

[getFieldPersistentValue](https://bryntum.com/docs/gantt/api/Core/data/Model#function-getFieldPersistentValue)
Returns field value that should be persisted, or `undefined` if field is configured with `persist: false`.

[clearChanges](https://bryntum.com/docs/gantt/api/Core/data/Model#function-clearChanges)
Clears tracked changes, used on commit. Does not revert changes.

[revertChanges](https://bryntum.com/docs/gantt/api/Core/data/Model#function-revertChanges)
Reverts changes in this back to their original values.

[generateId](https://bryntum.com/docs/gantt/api/Core/data/Model#function-generateId-static)
Generates an id for a new record (a phantom id), based on a UUID by default.

This function can be overridden to provide custom id generation logic.

```
let idCounter = 0;
// Override the default logic with app specific
Model.generateId = () => `id${new Date().getTime()}${idCounter++}`;
```

[generateId](https://bryntum.com/docs/gantt/api/Core/data/Model#function-generateId)
Generates an id for a new record (a phantom id), based on a UUID (starting with `_generated`).

Generated ids are intended to be temporary and should be replaced by the backend on commit.

[asId](https://bryntum.com/docs/gantt/api/Core/data/Model#function-asId-static)
Gets the id of specified model or model data object, or the value if passed string/number.

[toJSON](https://bryntum.com/docs/gantt/api/Core/data/Model#function-toJSON)
Used by `JSON.stringify()` to correctly convert this record to json.

In most cases no point in calling it directly.

```
// This will call `toJSON()`
const json = JSON.stringify(record);
```

If called manually, the resulting object is a clone of `record.data` + the data of any children:

```
const record = new Model({
    title    : 'Hello',
    children : [
        ...
    ]
});

const jsonObject = record.toJSON();

// jsonObject:
{
    title : 'Hello',
    children : [
        ...
    ]
}
```

[toString](https://bryntum.com/docs/gantt/api/Core/data/Model#function-toString)
Represent the record as a string, by default as a JSON string. Tries to use an abbreviated version of the object's data, using id + name/title/text/label/description. If no such field exists, the full data is used.

```
const record = new Model({ id : 1, name : 'Steve Rogers', alias : 'Captain America' });
console.log(record.toString()); // logs { "id" : 1, "name" : "Steve Rogers" }
```

[hasBatchedChange](https://bryntum.com/docs/gantt/api/Core/data/Model#function-hasBatchedChange)
Returns `true` if this Model currently has outstanding batched changes for the specified field name.

[beginBatch](https://bryntum.com/docs/gantt/api/Core/data/Model#function-beginBatch)
Begin a batch, which stores changes and commits them when the batch ends. Prevents events from being fired during batch.

```
record.beginBatch();
record.name = 'Mr Smith';
record.team = 'Golden Knights';
record.endBatch();
```

Please note that you can also set multiple fields in a single call using [set](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set), which in many cases can replace using a batch:

```
record.set({
  name : 'Mr Smith',
  team : 'Golden Knights'
});
```

[endBatch](https://bryntum.com/docs/gantt/api/Core/data/Model#function-endBatch)
End a batch, triggering events if data has changed.

[cancelBatch](https://bryntum.com/docs/gantt/api/Core/data/Model#function-cancelBatch)
Cancels current batch operation. Any changes during the batch are discarded.

[triggerBeforeUpdate](https://bryntum.com/docs/gantt/api/Core/data/Model#function-triggerBeforeUpdate)
Triggers beforeUpdate event for each store and checks if changes can be made from event return value.

[copy](https://bryntum.com/docs/gantt/api/Core/data/Model#function-copy)
Makes a copy of this model, assigning the specified id or a generated id and also allowing you to pass field values to the created copy. A [copyOf](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-copyOf) property is set on the copy to reference the original record.

```
const record = new Model({ name : 'Super model', hairColor : 'Brown' });
const clone = record.copy({ name : 'Super model clone' });
```

[remove](https://bryntum.com/docs/gantt/api/Core/data/Model#function-remove)
Removes this record from all stores (and in a tree structure, also from its parent if it has one).

[joinStore](https://bryntum.com/docs/gantt/api/Core/data/Model#function-joinStore)
Joins this record and any children to specified store, if not already joined.

[unjoinStore](https://bryntum.com/docs/gantt/api/Core/data/Model#function-unjoinStore)
Unjoins this record and any children from specified store, if already joined.

[isPartOfStore](https://bryntum.com/docs/gantt/api/Core/data/Model#function-isPartOfStore)
Returns `true` if this record is contained in the specified store, or in any store if store param is omitted.

[isEditable](https://bryntum.com/docs/gantt/api/Core/data/Model#function-isEditable)
Defines if the given event field should be manually editable in UI. You can override this method to provide your own logic.

[instanceMeta](https://bryntum.com/docs/gantt/api/Core/data/Model#function-instanceMeta)
Used to set per external instance meta data. For example useful when using a record in multiple grids to store some state per grid.

## Typedefs

Typedefs are type definitions for the class

[RelationConfig](https://bryntum.com/docs/gantt/api/Core/data/Model#typedef-RelationConfig)
Defines the properties of a relation between two stores.

Used as the values of a Model's [relations](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-relations-static) definition.

This snippet will define a relation called `team`, allowing access to the foreign record via `player.team`. It will point to a record in the `teamStore` (must be available as `record.firstStore.teamStore)` with an id matching the players `teamId` field. The team record in turn, will have a field called `players` which is a collection of all players in the team.

```
class Player extends Model {
    static relations = {
        team : {
            foreignKey            : 'teamId',
            foreignStore          : 'teamStore',
            relatedCollectionName : 'players'
        }
    }
}
```

See [relations](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-relations-static) for a more extensive example.
