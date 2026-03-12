# Source: https://bookshelfjs.org/api.html

Title: Bookshelf.js | API Reference

URL Source: https://bookshelfjs.org/api.html

Markdown Content:
Bookshelf.js Guides API Reference 
Bookshelf
CONSTRUCTION
Bookshelf
MEMBERS
knex
METHODS
model
plugin
resolve
transaction
Model
CONSTRUCTION
Model
initialize
STATIC
collection
count
extend
fetchAll
forge
MEMBERS
defaults
hasTimestamps
hidden
id
idAttribute
requireFetch
tableName
visible
METHODS
belongsTo
belongsToMany
clear
clone
count
destroy
escape
fetch
fetchAll
fetchPage
format
get
has
hasChanged
hasMany
hasOne
isNew
load
morphMany
morphOne
morphTo
off
on
once
orderBy
parse
previous
previousAttributes
query
refresh
related
resetQuery
save
serialize
set
through
timestamp
toJSON
trigger
triggerThen
unset
where
LODASH METHODS
omit
pick
EVENTS
counting
created
creating
destroyed
destroying
fetched
fetching
saved
saving
updated
updating
fetched:collection
fetching:collection
NoRowsDeletedError
CONSTRUCTION
NoRowsDeletedError
NoRowsUpdatedError
CONSTRUCTION
NoRowsUpdatedError
NotFoundError
CONSTRUCTION
NotFoundError
Collection
CONSTRUCTION
Collection
initialize
STATIC
extend
forge
MEMBERS
count
create
fetch
fetchOne
length
load
METHODS
add
at
attach
clone
detach
first
get
invokeThen
last
off
on
once
orderBy
parse
pluck
pop
push
query
reduceThen
remove
reset
serialize
set
shift
slice
through
toJSON
trigger
triggerThen
unshift
updatePivot
where
withPivot
LODASH METHODS
countBy
every
filter
find
forEach
groupBy
includes
invokeMap
isEmpty
map
reduce
reduceRight
reject
some
sortBy
toArray
EVENTS
fetched
EmptyError
CONSTRUCTION
EmptyError
Events
CONSTRUCTION
Events
METHODS
off
on
once
trigger
triggerThen
API REFERENCE
Bookshelf

The Bookshelf library is initialized by passing an initialized Knex client instance. The knex documentation provides a number of examples for different databases.

CONSTRUCTION
new Bookshelf(knex)
source
Parameters
knex Knex

Knex instance.

MEMBERS
bookshelf.knex :Knex
source

A reference to the Knex.js instance being used by Bookshelf.

METHODS
bookshelf.model(name, [Model], [staticProperties]) → Model
source
Example
// Defining and registering a model
module.exports = bookshelf.model('Customer', {
  tableName: 'customers',
  orders() {
    return this.hasMany('Order')
  }
})

// Retrieving a previously registered model
const Customer = bookshelf.model('Customer')

// Registering already defined models
// file: customer.js
const Customer = bookshelf.Model.extend({
  tableName: 'customers',
  orders() {
    return this.hasMany('Order')
  }
})
module.exports = bookshelf.model('Customer', Customer)

// file: order.js
const Order = bookshelf.Model.extend({
  tableName: 'orders',
  customer() {
    return this.belongsTo('Customer')
  }
})
module.exports = bookshelf.model('Order', Order)
Parameters
name string

The name to save the model as, or the name of the model to retrieve if no further arguments are passed to this method.

[Model] Model|Object

The model to register. If a plain object is passed it will be converted to a Model. See example above.

[staticProperties] Object

If a plain object is passed as second argument, this can be used to specify additional static properties and methods for the new model that is created.

Returns
Model

The registered model.

Registers a model. Omit the second argument Model to return a previously registered model that matches the provided name.

Note that when registering a model with this method it will also be available to all relation methods, allowing you to use a string name in that case. See the calls to hasMany() in the examples above.

bookshelf.plugin(plugin, options) → Bookshelf
source
Parameters
plugin string|array|function

The plugin or plugins to load. If you provide a string it can represent an npm package or a file somewhere on your project. You can also pass a function as argument to add it as a plugin. Finally, it's also possible to pass an array of strings or functions to add them all at once.

options mixed

This can be anything you want and it will be passed directly to the plugin as the second argument when loading it.

Returns
Bookshelf

The bookshelf instance for chaining.

This method provides a nice, tested, standardized way of adding plugins to a Bookshelf instance, injecting the current instance into the plugin, which should be a module.exports.

You can add a plugin by specifying a string with the name of the plugin to load. In this case it will try to find a module. It will pass the string to require(), so you can either require a third-party dependency by name or one of your own modules by relative path:

bookshelf.plugin('./bookshelf-plugins/my-favourite-plugin');
bookshelf.plugin('plugin-from-npm');


There are a few official plugins published in npm, along with many independently developed ones. See the list of available plugins.

You can also provide an array of strings or functions, which is the same as calling bookshelf.plugin() multiple times. In this case the same options object will be reused:

bookshelf.plugin(['cool-plugin', './my-plugins/even-cooler-plugin']);


Example plugin:

// Converts all string values to lower case when setting attributes on a model
module.exports = function(bookshelf) {
  bookshelf.Model = bookshelf.Model.extend({
    set(key, value, options) {
      if (!key) return this
      if (typeof value === 'string') value = value.toLowerCase()
      return bookshelf.Model.prototype.set.call(this, key, value, options)
    }
  })
}
bookshelf.resolve(name) → *
source
Example
const Customer = bookshelf.model('Customer', {
  tableName: 'customers'
})

bookshelf.resolve = (name) => {
  if (name === 'SpecialCustomer') return Customer;
}
Parameters
name string

The model name to resolve.

Returns
*

The return value will depend on what your re-implementation of this function does.

Override this in your bookshelf instance to define a custom function that will resolve the location of a model or collection when using the Bookshelf#model method or when passing a string with a model name in any of the collection methods (e.g. Model#hasOne, Model#hasMany, etc.).

This will only be used if the specified name cannot be found in the registry. Note that this function can return anything you'd like, so it's not restricted in functionality.

bookshelf.transaction(transactionCallback) → Promise
source
Example
var Promise = require('bluebird')

Bookshelf.transaction((t) => {
  return new Library({name: 'Old Books'})
    .save(null, {transacting: t})
    .tap(function(model) {
      return Promise.map([
        {title: 'Canterbury Tales'},
        {title: 'Moby Dick'},
        {title: 'Hamlet'}
      ], (info) => {
        return new Book(info).save({'shelf_id': model.id}, {transacting: t})
      })
    })
}).then((library) => {
  console.log(library.related('books').pluck('title'))
}).catch((err) => {
  console.error(err)
})
Parameters
transactionCallback Bookshelf~transactionCallback

Callback containing transaction logic. The callback should return a Promise.

Returns
Promise

A promise resolving to the value returned from transactionCallback.

An alias to Knex#transaction. The transaction object must be passed along in the options of any relevant Bookshelf calls, to ensure all queries are on the same connection. The entire transaction block is wrapped around a Promise that will commit the transaction if it resolves successfully, or roll it back if the Promise is rejected.

Note that there is no need to explicitly call transaction.commit() or transaction.rollback() since the entire transaction will be committed if there are no errors inside the transaction block.

When fetching inside a transaction it's possible to specify a row-level lock by passing the wanted lock type in the lock option to fetch. Available options are lock: 'forUpdate' and lock: 'forShare'.

TYPE DEFINITIONS
transactionCallback(transaction) → Promise
source
Parameters
transaction Transaction
See
Knex#transaction
Bookshelf#transaction
Returns
Promise

The Promise will resolve to the return value of the callback, or be rejected with an error thrown inside it. If it resolves, the entire transaction is committed, otherwise it is rolled back.

This is a transaction block to be provided to Bookshelf#transaction. All of the database operations inside it can be part of the same transaction by passing the transacting: transaction option to fetch, save or destroy.

Note that unless you explicitly pass the transaction object along to any relevant model operations, those operations will not be part of the transaction, even though they may be inside the transaction callback.

Model

Models are simple objects representing individual database rows, specifying the tableName and any relations to other models. They can be extended with any domain-specific methods, which can handle components such as validations, computed properties, and access control.

CONSTRUCTION
new Model(attributes, [options])
source
Parameters
attributes Object

Initial values for this model's attributes.

[options] Object

Hash of options.

[tableName] string

Initial value for tableName.

[hasTimestamps=false] Boolean

Initial value for hasTimestamps.

[parse=false] Boolean

Convert attributes by parse before being set on the model.

When defining a model you should use the bookshelf.model method, since it will allow you to avoid circular dependency problems. However, it's still possible to create models using the regular constructor.

When creating an instance of a model, you can pass in the initial values of the attributes, which will be set on the model. If you define an initialize function, it will be invoked when the model is created.

new Book({
  title: "One Thousand and One Nights",
  author: "Scheherazade"
});


In rare cases, if you're looking to get fancy, you may want to override constructor, which allows you to replace the actual constructor function for your model.

let Book = bookshelf.model('Book', {
  tableName: 'documents',
  constructor: function() {
    bookshelf.Model.apply(this, arguments);
    this.on('saving', function(model, attrs, options) {
      options.query.where('type', '=', 'book');
    });
  }
});
model.initialize(attributes, [options])
source
Parameters
attributes Object

Initial values for this model's attributes.

[options] Object

The hash of options passed to constructor.

See
Model

Called by the Model constructor when creating a new instance. Override this function to add custom initialization, such as event listeners. Because plugins may override this method in subclasses, make sure to call your super (extended) class. e.g.

initialize: function() {
    this.constructor.__super__.initialize.apply(this, arguments);
    // Your initialization code ...
}
STATIC
Model.collection([models], [options]) → Collection
source
Example
Customer.collection().fetch().then((customers) => {
  // ...
})
Parameters
[models] Model[]

Any models to be added to the collection.

[options] Object

Additional options to pass to the Collection constructor.

[comparator] string|function

If specified this is used to sort the collection. It can be a string representing the model attribute to sort by, or a custom function. Check the documentation for Array.prototype.sort for more info on how to use a custom comparator function. If this options is not specified the collection sort order depends on what the database returns.

Returns
Collection

The newly created collection. It will be empty unless any models were passed as the first argument.

A simple static helper to instantiate a new Collection, setting the model it's called on as the collection's target model.

Model.count([column], [options]) → Promise
source
Example
Duck.count().then((count) => {
  console.log('number of ducks', count)
})
Parameters
[column='*'] string

Specify a column to count. Rows with null values in this column will be excluded.

[options] Object

Hash of options.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Since
0.8.2
See
Model#count
Returns
Promise

Shortcut to a model's count method so you don't need to instantiate a new model to count the number of records.

Model.extend([prototypeProperties], [classProperties]) → function
source
Example
const Promise = require('bluebird')
const compare = require('some-crypt-library')

const Customer = bookshelf.model('Customer', {
  initialize() {
    this.constructor.__super__.initialize.apply(this, arguments)

    // Setting up a listener for the 'saving' event
    this.on('saving', this.validateSave)
  },

  validateSave() {
    return doValidation(this.attributes)
  },

  account() {
    // Defining a relation with the Account model
    return this.belongsTo(Account)
  }
}, {
  login: Promise.method(function(email, password) {
    if (!email || !password)
      throw new Error('Email and password are both required')

    return new this({email: email.toLowerCase()})
      .fetch()
      .tap(function(customer) {
        if (!compare(password, customer.get('password'))
          throw new Error('Invalid password')
      })
  })
})
Parameters
[prototypeProperties] Object

Instance methods and properties to be attached to instances of the new class.

[classProperties] Object

Class (i.e. static) functions and properties to be attached to the constructor of the new class.

Returns
function

Constructor for new Model subclass.

This static method allows you to create your own Model classes by extending bookshelf.Model.

It correctly sets up the prototype chain, which means that subclasses created this way can be further extended and subclassed as far as you need.

Model.fetchAll() → Promise<Collection>
source
See
Model#fetchAll
Returns
Promise<Collection>

Simple helper function for retrieving all instances of the given model.

Model.forge([attributes], [options])
source
Parameters
[attributes] Object

Initial values for this model's attributes.

[options] Object

Hash of options.

[tableName] string

Initial value for tableName.

[hasTimestamps=false] Boolean

Initial value for hasTimestamps.

[parse=false] Boolean

Convert attributes by parse before being set on the model.

A simple helper function to instantiate a new Model without needing new.

MEMBERS
model.defaults :Object|Null
source
Example
var MyModel = bookshelf.model('MyModel', {
  defaults: {property1: 'foo', property2: 'bar'},
  tableName: 'my_models'
})

MyModel.forge({property1: 'blah'}).save().then(function(model) {
  // {property1: 'blah', property2: 'bar'}
})

This can be used to define any default values for attributes that are not present when creating or updating a model in a save call. The default behavior is to not use these default values on updates unless the defaults: true option is passed to the save call. For inserts the default values will always be used if present.

model.hasTimestamps :Boolean|Array
source
Example
var MyModel = bookshelf.model('MyModel', {
  hasTimestamps: true,
  tableName: 'my_models'
})

var myModel = MyModel.forge({name: 'blah'}).save().then(function(savedModel) {
  // {
  //   name: 'blah',
  //   created_at: 'Sun Mar 25 2018 15:07:11 GMT+0100 (WEST)',
  //   updated_at: 'Sun Mar 25 2018 15:07:11 GMT+0100 (WEST)'
  // }
})

myModel.save({created_at: new Date(2015, 5, 2)}).then(function(updatedModel) {
  // {
  //   name: 'blah',
  //   created_at: 'Tue Jun 02 2015 00:00:00 GMT+0100 (WEST)',
  //   updated_at: 'Sun Mar 25 2018 15:07:11 GMT+0100 (WEST)'
  // }
})

Automatically sets the current date and time on the timestamp attributes created_at and updated_at based on the type of save method. The update method will only update updated_at, while the insert method will set both values.

To override the default attribute names, assign an array to this property. The first element will be the created column name and the second will be the updated one. If any of these elements is set to null that particular timestamp attribute will not be used in the model. For example, to automatically update only the created_at attribute set this property to ['created_at', null].

You can override the timestamp attribute values of a model and those values will be used instead of the automatic ones when saving.

model.hidden :null|Array
source
Example
const MyModel = bookshelf.model('MyModel', {
  tableName: 'my_models',
  hidden: ['password']
})

const myModel = MyModel.forge({
  name: 'blah',
  password: 'secure'
}).save().then(function(savedModel) {
  console.log(savedModel.toJSON())
  // {
  //   name: 'blah',
  //   created_at: 'Sun Mar 25 2018 15:07:11 GMT+0100 (WEST)',
  //   updated_at: 'Sun Mar 25 2018 15:07:11 GMT+0100 (WEST)'
  // }
})

List of model attributes to exclude from the output when serializing it. This works as a blacklist, and all attributes not present in this list will be shown when calling toJSON.

By default this is null which means that no attributes will be excluded from the output.

You can override this list by passing the {hidden: ['list']} option directly to the toJSON or serialize call.

If both the hidden and the visible model properties are set, the hidden list will take precedence.

model.id :number|string
source
Example
const Television = bookshelf.model('Television', {
  tableName: 'televisions',
  idAttribute: 'coolId'
})

new Television({coolId: 1}).fetch(tv => {
  tv.get('coolId') // 1
  tv.id // 1
})

A special property of models which represents their unique identifier, named by the idAttribute. If you set the id in the attributes hash, it will be copied onto the model as a direct property.

Models can be retrieved by their id from collections, and the id is used when fetching models and building model relations.

Note that a model's id property can always be accessed even when the value of its idAttribute is not 'id'.

model.idAttribute :string
source

This tells the model which attribute to expect as the unique identifier for each database row (typically an auto-incrementing primary key named 'id'). Note that if you are using parse and format (to have your model's attributes in camelCase, but your database's columns in snake_case, for example) this refers to the name returned by parse (myId), not the actual database column (my_id).

You can also get the parsed id attribute value by using the model's parsedIdAttribute method.

If the table you're working with does not have a Primary-Key in the form of a single column you'll have to override it with a getter that returns null. Overriding with undefined does not cascade the default behavior of the value 'id'. Such a getter in ES6 would look like get idAttribute() { return null }.

model.requireFetch :boolean
source
Example
// Default behavior
const MyModel = bookshelf.model('MyModel', {
  tableName: 'my_models'
})

new MyModel({id: 1}).fetch().catch(error => {
  // Will throw NotFoundError if there are no results
})

// Overriding the default behavior
const MyModel = bookshelf.model('MyModel', {
  requireFetch: false,
  tableName: 'my_models'
})

new MyModel({id: 1}).fetch(model => {
  // model will be null if there are no results
 })
Since
1.0.0

Allows defining the default behavior when there are no results when fetching a model from the database. This applies only when fetching a single model using fetch or Collection#fetchOne.

You can override this model option when fetching by passing the {require: false} or {require: true} option to any of the fetch methods mentioned above.

model.tableName :string
source
Example
var Television = bookshelf.model('Television', {
  tableName: 'televisions'
});

A required property for any database usage, The tableName property refers to the database table name the model will query against.

model.visible :null|Array
source
Example
const MyModel = bookshelf.model('MyModel', {
  tableName: 'my_models',
  visible: ['name', 'created_at']
})

const myModel = MyModel.forge({
  name: 'blah',
  password: 'secure'
}).save().then(function(savedModel) {
  console.log(savedModel.toJSON())
  // {
  //   name: 'blah',
  //   created_at: 'Sun Mar 25 2018 15:07:11 GMT+0100 (WEST)',
  // }
})

List of model attributes to include in the output when serializing it. This works as a whitelist, and all attributes not present in this list will be hidden when calling toJSON.

By default this is null which means that all attributes will be included in the output.

You can override this list by passing the {visible: ['list']} option directly to the toJSON or serialize call.

If both the hidden and the visible model properties are set, the hidden list will take precedence.

METHODS
model.belongsTo(Target, [foreignKey], [foreignKeyTarget]) → Model
source
Example
const Book = bookshelf.model('Book', {
  tableName: 'books',
  author() {
    return this.belongsTo('Author')
  }
})

// select * from `books` where id = 1
// select * from `authors` where id = book.author_id
Book.where({id: 1}).fetch({withRelated: ['author']}).then((book) => {
  console.log(JSON.stringify(book.related('author')))
})
Parameters
Target Model|string

Constructor of Model targeted by the join. Can be a string specifying a previously registered model with Bookshelf#model.

[foreignKey] string

Foreign key in this model. By default, the foreignKey is assumed to be the singular form of the Target model's tableName, followed by _id, or _{{idAttribute}} if the idAttribute property is set.

[foreignKeyTarget] string

Column in the Target model's table which foreignKey references. This is only needed in case it's other than Target model's id / idAttribute.

Returns
Model

The return value will always be a model, even if the relation doesn't exist, but in that case the relation will be null when serializing the model.

This relationship is used when a model is a member of another Target model.

It can be used in One-to-one associations as the inverse of a hasOne. It can also used in One-to-many associations as the inverse of hasMany, and is the "one" side of that association. In both cases, the belongsTo relationship is used for a model that is a member of another Target model, referenced by the foreignKey attribute in the current model.

model.belongsToMany(Target, [joinTableName], [foreignKey], [otherKey], [foreignKeyTarget], [otherKeyTarget]) → Collection
source
Example
const Account = bookshelf.model('Account', {
  tableName: 'accounts'
})

const User = bookshelf.model('User', {
  tableName: 'users',
  allAccounts() {
    return this.belongsToMany('Account')
  },
  adminAccounts() {
    return this.belongsToMany('Account').query({where: {access: 'admin'}})
  },
  viewAccounts() {
    return this.belongsToMany('Account').query({where: {access: 'readonly'}})
  }
})
Parameters
Target Model|string

Constructor of Model targeted by join. Can be a string specifying a previously registered model with Bookshelf#model.

[joinTableName] string

Name of the joining table. Defaults to the two table names ordered alphabetically and joined by an underscore.

[foreignKey] string

Foreign key in this model. By default, the foreignKey is assumed to be the singular form of this model's tableName, followed by _id / _{{idAttribute}}.

[otherKey] string

Foreign key in the Target model. By default, this is assumed to be the singular form of the Target model's tableName, followed by _id / _{{idAttribute}}.

[foreignKeyTarget] string

Column in this model's table which foreignKey references. This is only needed if it's not the default id / idAttribute.

[otherKeyTarget] string

Column in the Target model's table which otherKey references. This is only needed, if it's not the expected default of the Target model's id / idAttribute.

Returns
Collection

A new empty collection that is decorated with extra pivot helper methods. See the description below for more info.

Defines a many-to-many relation, where the current model is joined to one or more of a Target model through another table. The default name for the joining table is the two models' table names joined by an underscore, and ordered alphabetically. For example, a users table and an accounts table would have a joining table named accounts_users.

The default key names in the joining table are the singular versions of the model table names, followed by _id / _{{idAttribute}}. So in the above example the columns in the joining table would be user_id, account_id, and access, which is used as an example of how dynamic relations can be formed using different contexts.

To customize the keys or the tableName used for the join table, you may specify them in the arguments to the function call:

this.belongsToMany(Account, 'users_accounts', 'userId', 'accountId')


If you wish to create a belongsToMany association where the joining table has a primary key and extra attributes in the model, you may create a belongsToMany through relation:

const Doctor = bookshelf.model('Doctor', {
  patients() {
    return this.belongsToMany('Patient').through('Appointment')
  }
})

const Appointment = bookshelf.model('Appointment', {
  patient() {
    return this.belongsTo('Patient')
  },
  doctor() {
    return this.belongsTo('Doctor')
  }
})

const Patient = bookshelf.model('Patient', {
  doctors() {
    return this.belongsToMany('Doctor').through('Appointment')
  }
})


Collections returned by a belongsToMany relation are decorated with several pivot helper methods. If you need more information about these methods see attach, detach, updatePivot and withPivot.

model.clear() → Model
source
Returns
Model

This model.

Clear all attributes on the model.

model.clone() → Model
source
Returns
Model

Cloned instance of this model.

Returns a new instance of the model with identical attributes, including any relations from the cloned model.

model.count([column], [options]) → Promise
source
Example
new Duck().where('color', 'blue').count('name').then((count) => {
  console.log('number of blue ducks', count)
})
Parameters
[column='*'] string

Specify a column to count. Rows with null values in this column will be excluded.

[options] Object

Hash of options.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Since
0.8.2
Fires
"counting"
Returns
Promise

A promise resolving to the number of matching rows. By default this will be a number, except with PostgreSQL where it will be a string. Check the description to see how to return a number instead in this case.

Gets the number of matching records in the database, respecting any previous calls to Model#query. If the column argument is provided, records with a null value in that column will be excluded from the count.

Note that in PostgreSQL the result is a string by default. To read more about the reasons for this see the pull request that implemented it in the node-postgres database driver. If you're sure that the results will always be less than 253 (9007199254740991) you can override the default string parser like this:

require('pg').defaults.parseInt8 = true


Put this snippet before the call to require('knex') wherever you are initalizing knex.

model.destroy([options]) → Promise<Model>
source
Example
new User({id: 1})
  .destroy()
  .then(function(model) {
    // ...
  });
Parameters
[options] Object

Hash of options.

[transacting] Transaction

Optionally run the query in a transaction.

[require=true] Boolean

Throw a Model.NoRowsDeletedError if no records are affected by destroy. This is the default behavior as of version 0.13.0.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Fires
"destroying"
"destroyed"
Throws
Model.NoRowsDeletedError
Returns
Promise<Model>

A promise resolving to the destroyed and thus empty model, i.e. all attributes are undefined.

destroy performs a delete on the model, using the model's idAttribute to constrain the query.

A "destroying" event is triggered on the model before being destroyed. To prevent destroying the model, throwing an error inside one of the event listeners will stop destroying the model and reject the promise.

A "destroyed" event is fired after the model's removal is completed.

model.escape(attribute) → string
source
Parameters
attribute string

The attribute to escape.

Returns
string

HTML-escaped value of an attribute.

Get the HTML-escaped value of an attribute.

model.fetch([options]) → Promise<Model|null>
source
Parameters
[options] Object

Hash of options.

[require=true] Boolean

Whether or not to reject the returned response with a NotFoundError if there are no results when fetching. If set to false it will resolve with null instead.

[columns='*'] string|string[]

Specify columns to be retrieved.

[transacting] Transaction

Optionally run the query in a transaction.

[lock] string

Type of row-level lock to use. Valid options are forShare and forUpdate. This only works in conjunction with the transacting option, and requires a database that supports it.

[withRelated] string|Object|mixed[]

Relations to be retrieved with Model instance. Either one or more relation names or objects mapping relation names to query callbacks.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Fires
"fetching"
"fetched"
Throws
Model.NotFoundError
Returns
Promise<Model|null>

A promise resolving to the fetched model or null if none exists and the require: false option is passed.

Fetches a model from the database, using any attributes currently set on the model to constrain the results.

A "fetching" event will be fired just before the record is fetched; a good place to hook into for validation. "fetched" event will be fired when a record is successfully retrieved.

If you need to constrain the query performed by fetch, you can call query or where before calling fetch.

// select * from `books` where `ISBN-13` = '9780440180296'
new Book({'ISBN-13': '9780440180296'})
  .fetch()
  .then(function(model) {
    // outputs 'Slaughterhouse Five'
    console.log(model.get('title'));
  });


If you'd like to only fetch specific columns, you may specify a columns property in the options for the fetch call, or use query, tapping into the Knex column method to specify which columns will be fetched.

A single property, or an array of properties can be specified as a value for the withRelated property. You can also execute callbacks on relations queries (eg. for sorting a relation). The results of these relation queries will be loaded into a relations property on the model, may be retrieved with the related method, and will be serialized as properties on a toJSON call unless {shallow: true} is passed.

let Book = bookshelf.model('Book', {
  tableName: 'books',
  editions: function() {
    return this.hasMany('Edition');
  },
  chapters: function() {
    return this.hasMany('Chapter');
  },
  genre: function() {
    return this.belongsTo('Genre');
  }
})

new Book({'ISBN-13': '9780440180296'}).fetch({
  withRelated: [
    'genre', 'editions',
    { chapters: function(query) { query.orderBy('chapter_number'); }}
  ]
}).then(function(book) {
  console.log(book.related('genre').toJSON());
  console.log(book.related('editions').toJSON());
  console.log(book.toJSON());
});
model.fetchAll([options]) → Promise
source
Parameters
[options] Object

Set of options to modify the request.

[require=false] boolean

Whether or not to reject the returned Promise with a Collection.EmptyError if no records can be fetched from the database.

[transacting] Transaction

Optionally run the query in a transaction.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Fires
"fetching:collection"
"fetched:collection"
Throws
Collection.EmptyError

This error is used to reject the Promise in the event of an empty response from the database in case the require: true fetch option is used.

Returns
Promise

A Promise resolving to the fetched collection.

Fetches a collection of models from the database, using any query parameters currently set on the model to constrain the results.

Returns a Promise that will resolve with the fetched collection. If there are no results it will resolve with an empty collection. If instead you wish the Promise to be rejected with a Collection.EmptyError, pass the require: true option.

If you need to constrain the results, you can call the query or where methods before calling this method.

model.fetchPage([options]) → Promise<Collection>
source
Example
new Car()
  .fetchPage({
    pageSize: 15, // Defaults to 10 if not specified
    page: 3, // Defaults to 1 if not specified
    withRelated: ['engine'] // Passed to Model#fetchAll
  })
  .then(function(results) {
    console.log(results) // Paginated results object with metadata example below
  })

// Pagination results:
{
  models: [
    // Regular bookshelf Collection
  ],
  // other standard Collection attributes
  // ...
  pagination: {
    rowCount: 53, // Total number of rows found for the query before pagination
    pageCount: 4, // Total number of pages of results
    page: 3, // The requested page number
    pageSize: 15 // The requested number of rows per page
   }
}
Parameters
[options] Object

Besides the basic options that can be passed to Model#fetchAll, there are some additional pagination options that can be specified.

[pageSize] number

How many models to include in each page, defaulting to 10 if not specified. Used only together with the page option.

[page] number

Page number to retrieve. If greater than the available rows it will return an empty Collection. The first page is number 1. Used only with the pageSize option.

[limit] number

How many models to include in each page, defaulting to 10 if not specified. Used only together with the offset option.

[offset] number

Index to begin fetching results from. The default and initial value is 0. Used only with the limit option.

[disableCount=false] boolean

Whether to disable the query for counting how many records are in the full result.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Returns
Promise<Collection>

Returns a Promise that will resolve to the paginated collection of models.

This method is similar to Model#fetchAll, but fetches a single page of results as specified by the limit (page size) and offset (page number).

Any options that may be passed to Model#fetchAll may also be passed in the options to this method. Additionally, to perform pagination, you may include either an offset and limit, or a page and pageSize.

By default, with no parameters or some missing parameters, fetchPage will use default values of {page: 1, pageSize: 10}.

model.format(attributes) → Object
source
Parameters
attributes Object

The attributes to be converted.

Returns
Object

Formatted attributes.

The format method is used to modify the current state of the model before it is persisted to the database. The attributes passed are a shallow clone of the model, and are only used for inserting/updating - the current values of the model are left intact.

Do note that format is used to modify the state of the model when accessing the database, so if you remove an attribute in your format method, that attribute will never be persisted to the database, but it will also never be used when doing a fetch(), which may cause unexpected results. You should be very cautious with implementations of this method that may remove the primary key from the list of attributes.

If you need to modify the database data before it is given to the model, override the parse method instead. That method does the opposite operation of format.

model.get(attribute) → mixed
source
Example
note.get("title");
Parameters
attribute string

The name of the attribute to retrieve.

Returns
mixed

Attribute value.

Get the current value of an attribute from the model.

model.has(attribute) → Boolean
source
Parameters
attribute string

The attribute to check.

Returns
Boolean

True if attribute is set, otherwise false.

Returns true if the attribute contains a value that is not null or undefined.

model.hasChanged([attribute]) → Boolean
source
Example
Author.forge({id: 1}).fetch().then(function(author) {
  author.hasChanged() // false
  author.set('name', 'Bob')
  author.hasChanged('name') // true
})
Parameters
[attribute] string

A specific attribute to check for changes.

Returns
Boolean

true if any attribute has changed, false otherwise. Alternatively, if the attribute argument was specified, checks if that particular attribute has changed.

Returns true if any attribute has changed since the last fetch or save. If an attribute name is passed as argument, returns true only if that specific attribute has changed.

Note that even if an attribute is changed by using the set method, but the new value is exactly the same as the existing one, the attribute is not considered changed.

model.hasMany(Target, [foreignKey], [foreignKeyTarget]) → Collection
source
Example
const Author = bookshelf.model('Author', {
  tableName: 'authors',
  books() {
    return this.hasMany('Book')
  }
})

// select * from `authors` where id = 1
// select * from `books` where author_id = 1
Author.where({id: 1}).fetch({withRelated: ['books']}).then(function(author) {
  console.log(JSON.stringify(author.related('books')))
})
Parameters
Target Model|string

Constructor of Model targeted by join. Can be a string specifying a previously registered model with Bookshelf#model.

[foreignKey] string

ForeignKey in the Target model. By default, the foreign key is assumed to be the singular form of this model's tableName, followed by _id / _{{idAttribute}}.

[foreignKeyTarget] string

Column in this model's table which foreignKey references, if other than this model's id / idAttribute.

Returns
Collection

A new empty Collection.

This relation specifies that this model has one or more rows in another table which match on this model's primary key.

model.hasOne(Target, [foreignKey], [foreignKeyTarget]) → Model
source
Example
const Record = bookshelf.model('Record', {
  tableName: 'health_records'
})

const Patient = bookshelf.model('Patient', {
  tableName: 'patients',
  record() {
    return this.hasOne('Record')
  }
})

// select * from `health_records` where `patient_id` = 1
new Patient({id: 1}).related('record').fetch().then(function(model) {
  // ...
})

// Alternatively, if you don't need the relation loaded on the patient's relations hash:
new Patient({id: 1}).record().fetch().then(function(model) {
  // ...
})
Parameters
Target Model|string

Constructor of Model targeted by join. Can be a string specifying a previously registered model with Bookshelf#model.

[foreignKey] string

Foreign key in the Target model. By default the foreign key is assumed to be the singular form of this model's tableName followed by _id / _{{idAttribute}}.

[foreignKeyTarget] string

Column in this model's table which foreignKey references, if other than this model's id / idAttribute.

Returns
Model

The return value will always be a model, even if the relation doesn't exist, but in that case the relation will be null when serializing the model.

This relation specifies that this table has exactly one of another type of object, specified by a foreign key in the other table.

model.isNew()
source
Example
var modelA = new bookshelf.Model();
modelA.isNew(); // true

var modelB = new bookshelf.Model({id: 1});
modelB.isNew(); // false

Checks for the existence of an id to determine whether the model is considered "new".

model.load(relations, [options]) → Promise<Model>
source
Example
// Using an array of strings with relation names
new Posts().fetch().then(function(collection) {
  return collection.at(0).load(['author', 'content', 'comments.tags'])
}).then(function(model) {
  JSON.stringify(model)

  // {
  //   title: 'post title',
  //   author: {...},
  //   content: {...},
  //   comments: [
  //     {tags: [...]}, {tags: [...]}
  //   ]
  // }
})

// Using an object with query callbacks to filter the relations
new Posts().fetch().then(function(collection) {
  return collection.at(0).load({comments: function(qb) {
    qb.where('comments.is_approved', '=', true)
  }})
}).then(function(model) {
  JSON.stringify(model)
  // the model now includes all approved comments
})
Parameters
relations string|Object|mixed[]

The relation, or relations, to be loaded.

[options] Object

Hash of options.

[transacting] Transaction

Optionally run the query in a transaction.

[lock] string

Type of row-level lock to use. Valid options are forShare and forUpdate. This only works in conjunction with the transacting option, and requires a database that supports it.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Returns
Promise<Model>

A promise resolving to this model.

The load method takes an array of relations to eager load attributes onto a Model, in a similar way that the withRelated option works on fetch. Dot separated attributes may be used to specify deep eager loading.

It is possible to pass an object with query callbacks to filter the relations to eager load. An example is presented above.

model.morphMany(Target, [name], [columnNames], [morphValue]) → Collection
source
Parameters
Target Model|string

Constructor of Model targeted by join. Can be a string specifying a previously registered model with Bookshelf#model.

[name] string

Prefix for _id and _type columns.

[columnNames] string[]

Array containing two column names, the first is the _type while the second is the _id.

[morphValue=Target#tablename] string

The string value associated with this relationship. Stored in the _type column of the polymorphic table. Defaults to Target#tablename.

Returns
Collection

A collection of related models.

morphMany is essentially the same as a morphOne, but creating a collection rather than a model (similar to a hasOne vs. hasMany relation).

morphMany is used to signify a one-to-many or many-to-many polymorphic relation with another Target model, where the name of the model is used to determine which database table keys are used. The naming convention requires the name prefix an _id and _type field in the database. So for the case below the table names would be imageable_type and imageable_id. The morphValue may be optionally set to store/retrieve a different value in the _type column than the Target's tableName.

let Post = bookshelf.model('Post', {
  tableName: 'posts',
  photos: function() {
    return this.morphMany('Photo', 'imageable');
  }
});


And with custom columnNames:

let Post = bookshelf.model('Post'{
  tableName: 'posts',
  photos: function() {
    return this.morphMany('Photo', 'imageable', ['ImageableType', 'ImageableId']);
  }
});
model.morphOne(Target, [name], [columnNames], [morphValue]) → Model
source
Parameters
Target Model|string

Constructor of Model targeted by join. Can be a string specifying a previously registered model with Bookshelf#model.

[name] string

Prefix for _id and _type columns.

[columnNames] string[]

Array containing two column names, the first is the _type while the second is the _id.

[morphValue=Target#tableName] string

The string value associated with this relationship. Stored in the _type column of the polymorphic table. Defaults to Target#tableName.

Returns
Model

The related model.

The morphOne is used to signify a one-to-one polymorphic relation with another Target model, where the name of the model is used to determine which database table keys are used. The naming convention requires the name prefix an _id and _type field in the database. So for the case below the table names would be imageable_type and imageable_id. The morphValue may be optionally set to store/retrieve a different value in the _type column than the Model#tableName.

let Site = bookshelf.model('Site', {
  tableName: 'sites',
  photo: function() {
    return this.morphOne('Photo', 'imageable');
  }
});


And with custom columnNames:

let Site = bookshelf.model('Site', {
  tableName: 'sites',
  photo: function() {
    return this.morphOne('Photo', 'imageable', ['ImageableType', 'ImageableId']);
  }
});


Note that both columnNames and morphValue are optional arguments. How your argument is treated when only one is specified, depends on the type. If your argument is an array, it will be assumed to contain custom columnNames. If it's not, it will be assumed to indicate a morphValue.

model.morphTo(name, [columnNames], [Target]) → Model
source
Parameters
name string

Prefix for _id and _type columns.

[columnNames] string[]

Array containing two column names, where the first is the _type and the second is the _id.

[Target] Model|string

Constructor of Model targeted by join. Can be a string specifying a previously registered model with Bookshelf#model.

Returns
Model

The related but empty model.

This relation is used to specify the inverse of the morphOne or morphMany relations, where the targets must be passed to signify which models are the potential opposite end of the polymorphic relation:

const Photo = bookshelf.model('Photo', {
  tableName: 'photos',
  imageable() {
    return this.morphTo('imageable', 'Site', 'Post')
  }
})


And with custom column names:

const Photo = bookshelf.model('Photo', {
  tableName: 'photos',
  imageable() {
    return this.morphTo('imageable', ['ImageableType', 'ImageableId'], 'Site', 'Post')
  }
})


And with custom morphValues, the inverse of the morphValue of morphOne and morphMany, where the morphValues may be optionally set to check against a different value in the _type column other than the Model#tableName, for example, a more descriptive name, or a name that betters adheres to whatever standard you are using for models:

const Photo = bookshelf.model('Photo', {
  tableName: 'photos',
  imageable() {
    return this.morphTo('imageable', ['Site', 'favicon'], ['Post', 'cover_photo'])
  }
})
model.off()
source
Example
customer.off('fetched fetching');
ship.off(); // This will remove all event listeners
See
Events#off
model.on()
source
Example
customer.on('fetching', function(model) {
  // Do something before the data is fetched from the database
})
See
Events#on

Registers an event listener.

model.once(nameOrNames, callback)
source
Parameters
nameOrNames string

The name of the event or space separated list of events to register a callback for.

callback function

That callback to invoke only once when the event is fired.

Just like Events#on, but causes the bound callback to fire only once before being removed. Handy for saying "the next time that X happens, do this". When multiple events are passed in using the space separated syntax, the event will fire once for every event you passed in, not once for a combination of all events.

model.orderBy(sort, order)
source
Example
Car.forge().orderBy('color', 'ASC').fetchAll()
   .then(function (rows) { // ...
Parameters
sort string

Column to sort on

order string

Ascending ('ASC') or descending ('DESC') order

Since
0.9.3

Specifies the column to sort on and sort order.

The order parameter is optional, and defaults to 'ASC'. You may also specify 'DESC' order by prepending a hyphen to the sort column name. orderBy("date", 'DESC') is the same as orderBy("-date").

Unless specified using dot notation (i.e., "table.column"), the default table will be the table name of the model orderBy was called on.

model.parse(attributes) → Object
source
Example
// Example of a parser to convert snake_case to camelCase, using lodash
// This is just an example. You can use the official case converter plugin
// to achieve the same functionality.
model.parse = function(attrs) {
  return _.mapKeys(attrs, function(value, key) {
    return _.camelCase(key);
  });
};
Parameters
attributes Object

Hash of attributes to parse.

Returns
Object

Parsed attributes.

The parse method is called whenever a model's data is returned in a fetch call. The function is passed the raw database response object, and should return the attributes hash to be set on the model. The default implementation is a no-op, simply passing through the JSON response. Override this if you need to format the database responses - for example calling JSON.parse on a text field containing JSON, or explicitly typecasting a boolean in a sqlite3 database response.

If you need to format your data before it is saved to the database, override the format method in your models. That method does the opposite operation of parse.

model.previous(attribute) → mixed
source
Example
Author.forge({id: 1}).fetch().then(function(author) {
  author.get('name') // Alice
  author.set('name', 'Bob')
  author.previous('name') // 'Alice'
})
Parameters
attribute string

The attribute to check.

Returns
mixed

The previous value.

Returns the value of an attribute like it was before the last change. A change is usually done with the set method, but it can also be done with the save method. This is useful for getting back the original attribute value after it's been changed. It can also be used to get the original value after a model has been saved to the database or destroyed.

In case you want to get the previous value of all attributes at once you should use the previousAttributes method.

Note that this will return undefined if the model hasn't been fetched, saved, destroyed or eager loaded. However, in case one of these operations did take place, it will return the current value if an attribute hasn't changed. If you want to check if an attribute has changed see the hasChanged method.

model.previousAttributes() → Object
source
Example
Author.forge({id: 1}).fetch().then(function(author) {
  author.get('name') // Alice
  author.set('name', 'Bob')
  author.previousAttributes() // {id: 1, name: 'Alice'}
})

Author.forge({id: 1}).fetch().then(function(author) {
  author.get('name') // Alice
  return author.save({name: 'Bob'})
}).then(function(author) {
  author.get('name') // Bob
  author.previousAttributes() // {id: 1, name: 'Alice'}
})
Returns
Object

The attributes as they were before the last change, or an empty object in case the model data hasn't been fetched yet.

Returns a copy of the model's attributes like they were before the last change. A change is usually done with the set method, but it can also be done with the save method. This is mostly useful for getting a diff of the model's attributes after changing some of them. It can also be used to get the previous state of a model after it has been saved to the database or destroyed.

In case you want to get the previous value of a single attribute you should use the previous method.

Note that this will return an empty object if no changes have been made to the model and it hasn't been fetched, saved or eager loaded.

model.query(arguments) → Model|QueryBuilder
source
Example
model
  .query('where', 'other_id', '=', '5')
  .fetch()
  .then(function(model) {
    // ...
  });

model
  .query({where: {other_id: '5'}, orWhere: {key: 'value'}})
  .fetch()
  .then(function(model) {
    // ...
  });

model.query(function(qb) {
  qb.where('other_person', 'LIKE', '%Demo').orWhere('other_id', '>', 10);
}).fetch()
  .then(function(model) {
    // ...
  });

let qb = model.query();
qb.where({id: 1}).select().then(function(resp) {
  // ...
});
Parameters
arguments function|Object|string

The query method.

See
Knex `QueryBuilder`
Returns
Model|QueryBuilder

Will return this model or, if called with no arguments, the underlying query builder.

The query method is used to tap into the underlying Knex query builder instance for the current model. If called with no arguments, it will return the query builder directly. Otherwise, it will call the specified method on the query builder, applying any additional arguments from the model.query call. If the method argument is a function, it will be called with the Knex query builder as the context and the first argument, returning the current model.

model.refresh(options) → Promise<Model>
source
Parameters
options Object

A hash of options. See Model#fetch for details.

Since
0.8.2
Returns
Promise<Model>

A promise resolving to this model.

Update the attributes of a model, fetching it by its primary key. If no attribute matches its idAttribute, then fetch by all available fields.

model.related(name) → Model|Collection|undefined
source
Example
new Photo({id: 1}).fetch({
  withRelated: ['account']
}).then(function(photo) {
  var account = photo.related('account') // Get the eagerly loaded account

  if (account.id) {
    // Fetch a relation that has not been eager loaded yet
    return account.related('trips').fetch()
  }
})
Parameters
name string

The name of the relation to retrieve.

Returns
Model|Collection|undefined

The specified relation as defined by a method on the model, or undefined if it does not exist.

This method returns a specified relation loaded on the relations hash on the model, or calls the associated relation method and adds it to the relations hash if one exists and has not yet been loaded.

model.resetQuery() → Model
source
Returns
Model

Self, this method is chainable.

Used to reset the internal state of the current query builder instance. This method is called internally each time a database action is completed by Sync

model.save([attrs], [options]) → Promise<Model>
source
Example
// Save with no arguments
Model.forge({id: 5, firstName: 'John', lastName: 'Smith'}).save().then((model) => {
  //...
})

// Or add attributes during save
Model.forge({id: 5}).save({firstName: 'John', lastName: 'Smith'}).then((model) => {
  //...
})

// Or, if you prefer, for a single attribute
Model.forge({id: 5}).save('name', 'John Smith').then((model) => {
  //...
})
Parameters
[attrs] Object

Object containing the key: value pairs that you wish to save. If used with the patch option only these values will be saved and any values already set on the model will be ignored.

Instead of specifying this argument you can provide both a key and value arguments to save a single value. This is demonstrated in the example.

[options] Object
[transacting] Transaction

Optionally run the query in a transaction.

[method] string

Explicitly select a save method, either "update" or "insert".

[defaults=false] Boolean

Whether to assign or not default attribute values on a model when performing an update or create operation.

[patch=false] Boolean

Only save attributes supplied as arguments to the save call, ignoring any attributes that may be already set on the model.

[require=true] Boolean

Whether or not to throw a Model.NoRowsUpdatedError if no records are affected by save.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

[autoRefresh=true] boolean

Weather to enable auto refresh such that after a model is saved it will be populated with all the attributes that are present in the database, so you don't need to manually call refresh to update it. This will use two queries unless the database supports the RETURNING statement, in which case the model will be saved and its data fetched with a single query.

Fires
"saving"
"creating"
"updating"
"created"
"updated"
"saved"
Throws
Model.NoRowsUpdatedError
Returns
Promise<Model>

A promise resolving to the saved and updated model.

This method is used to perform either an insert or update query using the model's set attributes.

If the model isNew, any defaults will be set and an insert query will be performed. Otherwise it will update the record with a corresponding ID. It is also possible to set default attributes on an update by passing the {defaults: true} option in the second argument to the save call. This will also use the same defaults as the insert operation.

The type of operation to perform (either insert or update) can be overriden with the method option:

// This forces an insert with the specified id instead of the expected update
new Post({name: 'New Article', id: 34})
  .save(null, {method: 'insert'})
  .then((model) => {
    // ...
  })


If you only wish to update with the params passed to the save, you may pass a {patch: true} option in the second argument to save:

// UPDATE authors SET "bio" = 'Short user bio' WHERE "id" = 1
new Author({id: 1, first_name: 'User'})
  .save({bio: 'Short user bio'}, {patch: true})
  .then((model) => {
    // ...
  })


Several events fire on the model when starting the save process:

"creating" if the model is being inserted.
"updating" event if the model is being updated.
"saving" event in either case.

To prevent saving the model (for example, with validation), throwing an error inside one of these event listeners will stop the save process and reject the Promise.

If you wish to modify the query when the "saving" event is fired, the knex query object is available in options.query.

After the save is complete the following events will fire:

"created" if a new model was inserted in the database
"updated" if an existing model was updated.
"saved" event either way.

See the Events guide for further details.

model.serialize([options]) → Object
source
Example
var artist = new bookshelf.Model({
  firstName: "Wassily",
  lastName: "Kandinsky"
});

artist.set({birthday: "December 16, 1866"});

console.log(JSON.stringify(artist));
// {firstName: "Wassily", lastName: "Kandinsky", birthday: "December 16, 1866"}
Parameters
[options] Object
[shallow=false] Boolean

Whether to exclude relations from the output or not.

[omitPivot=false] Boolean

Whether to exclude pivot values from the output or not.

[hidden] Array

List of model attributes to exclude from the output.

[visible] Array

List of model attributes to include on the output. All other attributes will be hidden.

[visibility=true] Boolean

Whether to use visibility options or not. If set to false the hidden and visible options will be ignored.

Returns
Object

Serialized model as a plain object.

Return a copy of the model's attributes for JSON stringification. If the model has any relations defined, this will also call toJSON on each of the related objects, and include them on the object unless {shallow: true} is passed as an option.

You can define a whitelist of model attributes to include on the ouput with the {visible: ['list', 'of', 'attributes']} option. The {hidden: []} option produces the opposite effect, hiding attributes from the output.

This method is called internally by toJSON. Override this function if you want to customize its output.

model.set(attribute, [value], [options]) → Model
source
Example
customer.set({first_name: "Joe", last_name: "Customer"});
customer.set("telephone", "555-555-1212");
Parameters
attribute string|Object

Attribute name, or hash of attribute names and values.

[value] mixed

If a string was provided for attribute, the value to be set.

[options] Object
[unset=false] Object

Remove attributes from the model instead of setting them.

Returns
Model

This model.

Set a hash of attributes (one or many) on the model.

model.through(Interim, [throughForeignKey], [otherKey], [throughForeignKeyTarget], [otherKeyTarget]) → Model
source
Example
const Chapter = bookshelf.model('Chapter', {
  tableName: 'chapters',
  paragraphs() {
    return this.hasMany('Paragraph')
  }
})
const Book = bookshelf.model('Book', {
  tableName: 'books',
  chapters() {
    return this.hasMany('Chapter')
  }
})

     const Paragraph = bookshelf.model('Paragraph', {
  tableName: 'paragraphs',
  chapter() {
    return this.belongsTo('Chapter')
  },

  // Find the book where this paragraph is included, by passing through
  // the "Chapter" model.
  book() {
    return this.belongsTo('Book').through('Chapter')
  }
})
Parameters
Interim Model|string

Pivot model. Can be a string specifying a previously registered model with Bookshelf#model.

[throughForeignKey] string

Foreign key in this model. By default, the foreign key is assumed to be the singular form of the Target model's tableName, followed by _id or _{{idAttribute}}.

[otherKey] string

Foreign key in the Interim model. By default, the other key is assumed to be the singular form of this model's tableName, followed by _id / _{{idAttribute}}.

[throughForeignKeyTarget] string

Column in the Target model which throughForeignKey references, if other than Target model's id / idAttribute.

[otherKeyTarget] string

Column in this model which otherKey references, if other than id / idAttribute.

Returns
Model

The related but empty Model.

Helps to create dynamic relations between models where a hasOne or belongsTo relation may run through another Interim model. This is exactly like the equivalent collection method except that it applies to the models that the above mentioned relation methods return instead of collections.

This method creates a pivot model, which it assigns to model.pivot after it is created. When serializing the model with toJSON, the pivot model is flattened to values prefixed with _pivot_.

A good example of where this would be useful is if a paragraph belongsTo a book through a chapter. See the example above on how this can be expressed.

model.timestamp([options]) → Object
source
Parameters
[options] Object
[method] string

Either 'insert' or 'update' to specify what kind of save the attribute update is for.

[date] string

Either a Date object or ms since the epoch. Specify what date is used for updateing the timestamps, i.e. if something other than new Date() should be used.

Returns
Object

A hash of timestamp attributes that were set.

Automatically sets the timestamp attributes on the model, if hasTimestamps is set to true or an array. It checks if the model is new and sets the created_at and updated_at attributes (or any other custom attribute names you have set) to the current date. If the model is not new and is just being updated then only the updated_at attribute gets automatically updated.

If the model contains any user defined created_at or updated_at values, there won't be any automatic updated of these attributes and the user supplied values will be used instead.

model.toJSON([options])
source
Parameters
[options] Object

Options passed to Model#serialize.

Called automatically by JSON.stringify. To customize serialization, override serialize.

model.trigger()
source
Example
ship.trigger('fetched');
See
Events#trigger
model.triggerThen(name, […args]) → Promise
source
Parameters
name string

The event name or a whitespace-separated list of event names to be triggered.

[…args] mixed

Arguments to be passed to any registered event handlers.

Returns
Promise

A promise resolving to the return values of any triggered handlers.

A promise version of Events#trigger, returning a promise which resolves with all return values from triggered event handlers. If any of the event handlers throw an Error or return a rejected promise, the promise will be rejected. Used internally on the "creating", "updating", "saving", and "destroying" events, and can be helpful when needing async event handlers (e.g. for validations).

model.unset(attribute) → Model
source
Parameters
attribute

Attribute to unset.

Returns
Model

This model.

Remove an attribute from the model. unset is a noop if the attribute doesn't exist.

Note that unsetting an attribute from the model will not affect the related record's column value when saving the model. In order to clear the value of a column in the database record, set the attribute value to null instead: model.set("column_name", null).

model.where(method) → Model
source
Example
model.where('favorite_color', '<>', 'green').fetch().then(function() { //...
// or
model.where('favorite_color', 'red').fetch().then(function() { //...
// or
model.where({favorite_color: 'red', shoe_size: 12}).fetch().then(function() { //...
Parameters
method Object|string

Either key, [operator], value syntax, or a hash of attributes to match. Note that these must be formatted as they are in the database, not how they are stored after Model#parse.

See
Model#query
Returns
Model

Self, this method is chainable.

The where method is used as convenience for the most common query method, adding a where clause to the builder. Any additional knex methods may be accessed using query.

Accepts either key, value syntax, or a hash of attributes.

LODASH METHODS
omit()
pick()
EVENTS
model.on("counting", (model, options) =>
source
Parameters
model Model

The model firing the event.

options Object

Options object passed to count.

Tutorials
Events
Returns
Promise

Counting event.

Fired before a count query. A promise may be returned from the event handler for async behaviour.

model.on("created", (model, options) =>
source
Parameters
model Model

The model firing the event with its attributes matching what's in the database.

options Object

Options object passed to save.

Tutorials
Events
Returns
Promise

Created event.

Fired after an insert query.

model.on("creating", (model, attrs, options) =>
source
Parameters
model Model

The model firing the event.

attrs Object

Attributes that will be inserted.

options Object

Options object passed to save.

query QueryBuilder

Query builder to be used for saving. This can be used to modify or add to the query before it is executed.

Tutorials
Events
Returns
Promise

Creating event.

Fired before an insert query. A Promise may be returned from the event handler for async behaviour. Throwing an exception from the handler will cancel the save process.

model.on("destroyed", (model, options) =>
source
Parameters
model Model

The model firing the event.

options Object

Options object passed to destroy.

Tutorials
Events
Returns
Promise

Destroyed event.

Fired after a delete query. A promise may be returned from the event handler for async behaviour.

model.on("destroying", (model, options) =>
source
Parameters
model Model

The model firing the event.

options Object

Options object passed to destroy.

Tutorials
Events
Returns
Promise

Destroying event.

Fired before a delete query. A promise may be returned from the event handler for async behaviour. Throwing an exception from the handler will reject the promise and cancel the deletion.

model.on("fetched", (model, response, options) =>
source
Parameters
model Model

The model firing the event.

response Object

Knex query response.

options Object

Options object passed to fetch.

Tutorials
Events
Returns
Promise

If the handler returns a promise, fetch will wait for it to be resolved.

Fired after a fetch operation. A promise may be returned from the event handler for async behaviour.

model.on("fetching", (model, columns, options) =>
source
Example
const MyModel = bookshelf.model('MyModel', {
  initialize() {
    this.on('fetching', function(model, columns, options) {
      options.query.where('status', 'active')
    })
  }
})
Parameters
model Model

The model which is about to be fetched.

columns string[]

The columns to be retrieved by the query.

options Object

Options object passed to fetch.

query QueryBuilder

Query builder to be used for fetching. This can be used to modify or add to the query before it is executed. See example above.

Tutorials
Events
Returns
Promise

Fired before a fetch operation. A promise may be returned from the event handler for async behaviour.

model.on("saved", (model, options) =>
source
Parameters
model Model

The model firing the event with its attributes matching what's in the database.

options Object

Options object passed to save.

Tutorials
Events
Returns
Promise

Saved event.

Fired after an insert or update query.

model.on("saving", (model, attrs, options) =>
source
Parameters
model Model

The model firing the event. Its attributes are already changed but not commited to the database yet.

attrs Object

Attributes that will be inserted or updated.

options Object

Options object passed to save.

query QueryBuilder

Query builder to be used for saving. This can be used to modify or add to the query before it is executed.

Tutorials
Events
Returns
Promise

Saving event.

Fired before an insert or update query. A Promise may be returned from the event handler for async behaviour. Throwing an exception from the handler will cancel the save process.

model.on("updated", (model, options) =>
source
Parameters
model Model

The model firing the event with its attributes matching what's in the database.

options Object

Options object passed to save.

Tutorials
Events
Returns
Promise

Updated event.

Fired after an update query.

model.on("updating", (model, attrs, options) =>
source
Parameters
model Model

The model firing the event. Its attributes are already changed but not commited to the database yet.

attrs Object

Attributes that will be updated.

options Object

Options object passed to save.

query QueryBuilder

Query builder to be used for saving. This can be used to modify or add to the query before it is executed.

Tutorials
Events
Returns
Promise

Updating event.

Fired before an update query. A Promise may be returned from the event handler for async behaviour. Throwing an exception from the handler will cancel the save process.

model.on("fetched:collection", (collection, response, options) =>
source
Parameters
collection Collection

The collection that has been fetched.

response Object

The raw response from the underlying query builder. This will be an array with objects representing each row, similar to the output of a serialized Model.

options Object

Options object passed to fetchAll.

Tutorials
Events
Returns
Promise

Fired after a fetchAll operation. A promise may be returned from the event handler for async behaviour.

model.on("fetching:collection", (collection, columns, options) =>
source
Parameters
collection Collection

The collection that is going to be fetched. At this point it's still empty since the fetch hasn't happened yet.

columns string[]

The columns to be retrieved by the query as provided by the underlying query builder. If the columns option is not specified the value of this will usually be an array with a single string 'tableName.*'.

options Object

Options object passed to fetchAll.

Tutorials
Events
Returns
Promise

Fired before a fetchAll operation. A promise may be returned from the event handler for async behaviour.

Model.NoRowsDeletedError
CONSTRUCTION
new Model.NoRowsDeletedError()
source

Thrown when no record is deleted by destroy unless called with the {require: false} option.

Model.NoRowsUpdatedError
CONSTRUCTION
new Model.NoRowsUpdatedError()
source

Thrown when no records are saved by save unless called with the {require: false} option.

Model.NotFoundError
CONSTRUCTION
new Model.NotFoundError()
source

Thrown when no records are found by fetch or refresh unless called with the {require: false} option.

Collection

Collections are ordered sets of models returned from the database, from a fetchAll call.

CONSTRUCTION
new Collection([models], [options])
source
Example
const TabSet = bookshelf.collection('TabSet', {
  model: Tab
})
const tabs = new TabSet([tab1, tab2, tab3])
Parameters
[models] Model[]

Initial array of models.

[options] Object
[comparator=false] Boolean

Comparator for collection, or false to disable sorting.

When creating a Collection, you may choose to pass in the initial array of models. The collection's comparator may be included as an option. Passing false as the comparator option will prevent sorting. If you define an initialize function, it will be invoked when the collection is created.

If you would like to customize the Collection used by your models when calling Model#fetchAll or Model#fetchPage you can use the following process:

const Test = bookshelf.model('Test', {
  tableName: 'test'
}, {
  collection(...args) {
    return new Tests(...args)
  }
})
const Tests = bookshelf.collection('Tests', {
  get model() {
    return Test
  },
  initialize () {
    this.constructor.__super__.initialize.apply(this, arguments)
    // Collection will emit fetching event as expected even on eager queries.
    this.on('fetching', () => {})
  },
  doStuff() {
    // This method will be available in the results collection returned
    // by Test.fetchAll() and Test.fetchPage()
  }
})
collection.initialize()
source
See
Collection

Called by the Collection constructor when creating a new instance. Override this function to add custom initialization, such as event listeners. Because plugins may override this method in subclasses, make sure to call your super (extended) class. e.g.

initialize: function() {
  this.constructor.__super__.initialize.apply(this, arguments);
  // Your initialization code ...
}
STATIC
Collection.extend([prototypeProperties], [classProperties]) → function
source
Parameters
[prototypeProperties] Object

Instance methods and properties to be attached to instances of the new class.

[classProperties] Object

Class (ie. static) functions and properties to be attached to the constructor of the new class.

Returns
function

Constructor for new Collection subclass.

To create a Collection class of your own, extend Bookshelf.Collection.

Collection.forge([models], options)
source
Example
var Promise = require('bluebird');
var Accounts = bookshelf.Collection.extend({
  model: Account
});

var accounts = Accounts.forge([
  {name: 'Person1'},
  {name: 'Person2'}
]);

Promise.all(accounts.invokeMap('save')).then(function() {
  // collection models should now be saved...
});
Parameters
[models] Object[]|Model[]

Set of models (or attribute hashes) with which to initialize the collection.

options Object

Hash of options.

A simple helper function to instantiate a new Collection without needing new.

MEMBERS
collection.count
source
Example
// select count(*) from shareholders where company_id = 1 and share &gt; 0.1;
new Company({id: 1})
  .shareholders()
  .where('share', '>', '0.1')
  .count()
  .then((count) => {
    assert(count === 3)
  })
Parameters
[column='*'] string

Specify a column to count. Rows with null values in this column will be excluded.

[options] Object

Hash of options.

Since
0.8.2
See
Model#count
Returns
Promise

Get the number of records in the collection's table.

collection.create
source
Example
const { courses, ...attributes } = req.body;

Student.forge(attributes).save().tap(student =>
  Promise.map(courses, course => student.related('courses').create(course))
).then(student =>
  res.status(200).send(student)
).catch(error =>
  res.status(500).send(error.message)
);
Parameters
model Object

A set of attributes to be set on the new model.

[options] Object
[transacting] Transaction
[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Returns
Promise<Model>

A promise resolving with the new model.

Convenience method to create a new model instance within a collection. Equivalent to instantiating a model with a hash of attributes, saving the model to the database then adding the model to the collection.

When used on a relation, create will automatically set foreign key attributes before persisting the Model.

collection.fetch
source
Parameters
[options] Object
[require=false] Boolean

Whether or not to throw a Collection.EmptyError if no records are found. You can pass the require: true option to override this behavior.

[withRelated=[]] string|string[]

A relation, or list of relations, to be eager loaded as part of the fetch operation.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Fires
"fetched"
Throws
Collection.EmptyError

Thrown if no records are found.

Returns
Promise<Collection>

Fetch the default set of models for this collection from the database, resetting the collection when they arrive. If you wish to trigger an error if the fetched collection is empty, pass {require: true} as one of the options to the fetch call. A "fetched" event will be fired when records are successfully retrieved. If you need to constrain the query performed by fetch, you can call the query method before calling fetch.

If you'd like to only fetch specific columns, you may specify a columns property in the options for the fetch call.

The withRelated option may be specified to fetch the models of the collection, eager loading any specified relations named on the model. A single property, or an array of properties can be specified as a value for the withRelated property. The results of these relation queries will be loaded into a relations property on the respective models, may be retrieved with the related method.

collection.fetchOne
source
Example
// select * from authors where site_id = 1 and id = 2 limit 1;
new Site({id:1})
  .authors()
  .query({where: {id: 2}})
  .fetchOne()
  .then(function(model) {
    // ...
  });
Parameters
[options] Object
[require=true] Boolean

Whether or not to reject the returned Promise with a Model.NotFoundError if no records can be fetched from the database.

[columns='*'] string|string[]

Limit the number of columns fetched.

[transacting] Transaction

Optionally run the query in a transaction.

[lock] string

Type of row-level lock to use. Valid options are forShare and forUpdate. This only works in conjunction with the transacting option, and requires a database that supports it.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Throws
Model.NotFoundError
Returns
Promise<Model|null>

A promise resolving to the fetched Model or null if none exists and the require: false option is passed or requireFetch is set to false.

Fetch and return a single model from the collection, maintaining any relation data from the collection, and any query parameters that have already been passed to the collection. Especially helpful on relations, where you would only like to return a single model from the associated collection.

collection.length :Number
source
Example
var vanHalen = new bookshelf.Collection([eddie, alex, stone, roth]);
console.log(vanHalen.length) // 4

This is the total number of models in the collection. Note that this may not represent how many models there are in total in the database.

collection.load
source
Parameters
relations string|string[]

The relation, or relations, to be loaded.

[options] Object

Hash of options.

[transacting] Transaction
[lock] string

Type of row-level lock to use. Valid options are forShare and forUpdate. This only works in conjunction with the transacting option, and requires a database that supports it.

[debug=false] boolean

Whether to enable debugging mode or not. When enabled will show information about the queries being run.

Returns
Promise<Collection>

A promise resolving to this collection.

This method is used to eager load relations onto a Collection, in a similar way that the withRelated property works on fetch. Nested eager loads can be specified by separating the nested relations with ..

METHODS
collection.add(models, [options]) → Collection
source
Example
const ships = new bookshelf.Collection;

ships.add([
  {name: "Flying Dutchman"},
  {name: "Black Pearl"}
]);
Parameters
models Object[]|Model[]|Object|Model

One or more models or raw attribute objects.

[options] Object

Options for controlling how models are added.

[merge=false] Boolean

If set to true it will merge the attributes of duplicate models with the attributes of existing models in the collection.

[at] Number

If set to a number equal to or greater than 0 it will splice the model into the collection at the specified index number.

Returns
Collection

Self, this method is chainable.

Add a model, or an array of models, to the collection. You may also pass raw attribute objects, which will be converted to proper models when being added to the collection.

You can pass the {at: index} option to splice the model into the collection at the specified index.

By default if you're adding models to the collection that are already present, they'll be ignored, unless you pass {merge: true}, in which case their attributes will be merged with the corresponding models.

collection.at()
source

Get a model from a collection, specified by index. Useful if your collection is sorted, and if your collection isn't sorted, at will still retrieve models in insertion order.

collection.attach(ids, options) → Promise<Collection>
source
Parameters
ids mixed|mixed[]

One or more ID values or models to be attached to the relation.

options Object

A hash of options.

transacting Transaction

Optionally run the query in a transaction.

Returns
Promise<Collection>

A promise resolving to the updated Collection where this method was called.

Attaches one or more ids or models from a foreign table to the current table, on a many-to-many relation. Creates and saves a new model and attaches the model with the related model.

var admin1 = new Admin({username: 'user1', password: 'test'});
var admin2 = new Admin({username: 'user2', password: 'test'});

Promise.all([admin1.save(), admin2.save()])
  .then(function() {
    return Promise.all([
    new Site({id: 1}).admins().attach([admin1, admin2]),
    new Site({id: 2}).admins().attach(admin2)
  ]);
})


This method (along with Collection#detach and Collection#updatePivot) are mixed in to a Collection when returned by a belongsToMany relation.

collection.clone()
source
Overrides
CollectionBase#clone

Create a new collection with an identical list of models as this one.

collection.detach([ids], options) → Promise
source
Parameters
[ids] mixed|mixed[]

One or more ID values or models to be detached from the relation.

options Object

A hash of options.

transacting Transaction

Optionally run the query in a transaction.

Returns
Promise

A promise resolving to the updated Collection where this method was called.

Detach one or more related objects from their pivot tables. If a model or id is passed, it attempts to remove from the pivot table based on that foreign key. If no parameters are specified, we assume we will detach all related associations.

This method (along with Collection#attach and Collection#updatePivot) are mixed in to a Collection when returned by a belongsToMany relation.

collection.first() → Model|undefined
source
Returns
Model|undefined

The first model or undefined.

Returns the first model in the collection or undefined if the collection is empty.

collection.get() → Model
source
Example
const book = library.get(110);
Returns
Model

The model, or undefined if it is not in the collection.

Get a model from a collection, specified by an id, a cid, or by passing in a model.

collection.invokeThen(method, …arguments) → Promise
source
Parameters
method string

The model method to invoke.

…arguments mixed

Arguments to method.

Returns
Promise

Promise resolving to array of results from invocation.

Shortcut for calling Promise.all around a Collection#invoke, this will delegate to the collection's invoke method, resolving the promise with an array of responses all async (and sync) behavior has settled. Useful for bulk saving or deleting models:

collection.invokeThen('save', null, options).then(function() {
  // ... all models in the collection have been saved
});

collection.invokeThen('destroy', options).then(function() {
  // ... all models in the collection have been destroyed
});
collection.last() → Model|undefined
source
Returns
Model|undefined

The last model or undefined.

Returns the last model in the collection or undefined if the collection is empty.

collection.off()
source
Example
ships.off('fetched') // Remove the 'fetched' event listener
See
Events#off
collection.on()
source
Example
const ships = new bookshelf.Collection
ships.on('fetched', function(collection) {
  // Do something after the data has been fetched from the database
})
See
Events#on

Registers an event listener.

collection.once(nameOrNames, callback)
source
Parameters
nameOrNames string

The name of the event or space separated list of events to register a callback for.

callback function

That callback to invoke only once when the event is fired.

Just like Events#on, but causes the bound callback to fire only once before being removed. Handy for saying "the next time that X happens, do this". When multiple events are passed in using the space separated syntax, the event will fire once for every event you passed in, not once for a combination of all events.

collection.orderBy(column, order)
source
Example
Cars.forge().orderBy('color', 'ASC').fetch()
   .then(function (rows) { // ...
Parameters
column string

Column to sort on.

order string

Ascending ('ASC') or descending ('DESC') order.

Since
0.9.3

Specifies the column to sort on and sort order.

The order parameter is optional, and defaults to 'ASC'. You may also specify 'DESC' order by prepending a hyphen to the sort column name. orderBy("date", 'DESC') is the same as orderBy("-date").

Unless specified using dot notation (i.e., "table.column"), the default table will be the table name of the model orderBy was called on.

collection.parse(resp)
source
Parameters
resp Object[]

Raw database response array.

The parse method is called whenever a collection's data is returned in a fetch call. The function is passed the raw database response array, and should return an array to be set on the collection. The default implementation is a no-op, simply passing through the JSON response.

collection.pluck() → mixed[]
source
Returns
mixed[]

An array of attribute values.

Pluck an attribute from each model in the collection.

collection.pop()
source

Remove a model from the end of the collection.

collection.push(model) → Collection
source
Parameters
model Object[]|Model[]|Object|Model

One or more models or raw attribute objects.

Returns
Collection

Self, this method is chainable.

Add a model to the end of the collection.

collection.query(arguments) → Collection|QueryBuilder
source
Example
let qb = collection.query();
    qb.where({id: 1}).select().then(function(resp) {
      // ...
    });

collection.query(function(qb) {
  qb.where('id', '>', 5).andWhere('first_name', '=', 'Test');
}).fetch()
  .then(function(collection) {
    // ...
  });

collection
  .query('where', 'other_id', '=', '5')
  .fetch()
  .then(function(collection) {
    // ...
  });
Parameters
arguments function|Object|string

The query method.

See
Knex `QueryBuilder`
Returns
Collection|QueryBuilder

This collection or, if called with no arguments, the underlying query builder.

This method is used to tap into the underlying Knex query builder instance for the current collection.

If called with no arguments, it will return the query builder directly, otherwise it will call the specified method on the query builder, applying any additional arguments from the collection.query call.

If the method argument is a function, it will be called with the Knex query builder as the context and the first argument.

collection.reduceThen(iterator, initialValue, context) → Promise
source
Parameters
iterator Collection~reduceThenIterator
initialValue mixed
context Object

Bound to this in the iterator callback.

See
Bluebird `Promise.reduce` reference.
Returns
Promise

Promise resolving to the single result from the reduction.

Iterate over all the models in the collection and reduce this array to a single value using the given iterator function.

collection.remove(models, [options]) → Model|Model[]
source
Parameters
models Model|Model[]

The model, or models, to be removed.

[options] Object

Set of options for the operation.

[silent] Boolean

If set to true will not trigger a remove event on the removed model.

Returns
Model|Model[]

The same value passed in the models argument.

Remove a model, or an array of models, from the collection. Note that this does not remove the affected models from the database. For that purpose you have to use the model's destroy method.

If you wish to actually remove all the models in a collection from the database you can use this method:

myCollection.invokeThen('destroy').then(() => {
  // models have been destroyed
})
collection.reset(models, options) → Model[]
source
Parameters
models Object[]|Model[]|Object|Model

One or more models or raw attribute objects.

options Object

See add.

Returns
Model[]

Array of models.

Adding and removing models one at a time is all well and good, but sometimes you have so many models to change that you'd rather just update the collection in bulk. Use reset to replace a collection with a new list of models (or attribute hashes). Calling collection.reset() without passing any models as arguments will empty the entire collection.

collection.serialize([options]) → Object
source
Parameters
[options] Object
[shallow=false] Boolean

Exclude relations.

[omitPivot=false] Boolean

Exclude pivot values.

[omitNew=false] Boolean

Exclude models that return true for isNew.

Returns
Object

Serialized model as a plain object.

Return a raw array of the collection's attributes for JSON stringification. If the models have any relations defined, this will also call toJSON on each of the related objects, and include them on the object unless {shallow: true} is passed as an option.

serialize is called internally by toJSON. Override this function if you want to customize its output.

collection.set(models, [options]) → Collection
source
Example
var vanHalen = new bookshelf.Collection([eddie, alex, stone, roth]);
vanHalen.set([eddie, alex, stone, hagar]);
Parameters
models Object[]|Model[]|Object|Model

One or more models or raw attribute objects.

[options] Object

Options for controlling how models are added or removed.

[add=true] Boolean

If set to true it will add any new models to the collection, otherwise any new models will be ignored.

[merge=true] Boolean

If set to true it will merge the attributes of duplicate models with the attributes of existing models in the collection, otherwise duplicate models in the list will be ignored.

[remove=true] Boolean

If set to true any models in the collection that are not in the list will be removed from the collection, otherwise they will be kept.

Returns
Collection

Self, this method is chainable.

The set method performs a smart update of the collection with the passed model or list of models by following the following rules:

If a model in the list isn't yet in the collection it will be added
if the model is already in the collection its attributes will be merged
if the collection contains any models that aren't present in the list, they'll be removed.

If you'd like to customize the behavior, you can do so with the add, merge and remove options.

Since version 0.14.0 if both remove and merge options are set to false, then any duplicate models present will be added to the collection, otherwise they will either be removed or merged, according to the chosen option.

collection.shift()
source

Remove a model from the beginning of the collection.

collection.slice()
source

Slice out a sub-array of models from the collection.

collection.through(Interim, [throughForeignKey], [otherKey], [throughForeignKeyTarget], [otherKeyTarget]) → Collection
source
Example
const Chapter = bookshelf.model('Chapter', {
  tableName: 'chapters',
  paragraphs() {
    return this.hasMany(Paragraph)
  }
})

const Paragraph = bookshelf.model('Paragraph', {
  tableName: 'paragraphs',
  chapter() {
    return this.belongsTo(Chapter)
  }
})

const Book = bookshelf.model('Book', {
  tableName: 'books',
  // Find all paragraphs associated with this book, by
  // passing through the "Chapter" model.
  paragraphs() {
    return this.hasMany(Paragraph).through(Chapter)
  }
})
Parameters
Interim Model

Pivot model.

[throughForeignKey] string

Foreign key in this collection's model. This is the model that the hasMany or belongsToMany relations return. By default, the foreignKey is assumed to be the singular form of the Target model's tableName, followed by _id / _{{idAttribute}}.

[otherKey] string

Foreign key in the Interim model. By default, the otherKey is assumed to be the singular form of this model's tableName, followed by _id / _{{idAttribute}}.

[throughForeignKeyTarget] string

Column in this collection's model which throughForeignKey references, if other than the default of the model's id / idAttribute.

[otherKeyTarget] string

Column in the Interim model which otherKey references, if other than id / idAttribute.

Returns
Collection

The related but empty collection.

Used to define relationships where a hasMany or belongsToMany relation passes "through" an Interim model. This is exactly like the equivalent model method except that it applies to the collections that the above mentioned relation methods return instead of individual models.

A good example of where this would be useful is if a book hasMany paragraphs through chapters. See the example above for how this can be used.

collection.toJSON(Options)
source
Parameters
Options options

passed to Collection#serialize.

Called automatically by JSON.stringify. To customize serialization, override serialize.

collection.trigger()
source
Example
ships.trigger('fetched')
See
Events#trigger
collection.triggerThen(name, […args]) → Promise
source
Parameters
name string

The event name or a whitespace-separated list of event names to be triggered.

[…args] mixed

Arguments to be passed to any registered event handlers.

Returns
Promise

A promise resolving to the return values of any triggered handlers.

A promise version of Events#trigger, returning a promise which resolves with all return values from triggered event handlers. If any of the event handlers throw an Error or return a rejected promise, the promise will be rejected. Used internally on the "creating", "updating", "saving", and "destroying" events, and can be helpful when needing async event handlers (e.g. for validations).

collection.unshift()
source

Add a model to the beginning of the collection.

collection.updatePivot(attributes, [options]) → Promise
source
Parameters
attributes Object

Values to be set in the update query.

[options] Object

A hash of options.

[query] function|Object

Constrain the update query. Similar to the method argument to Model#query.

[require=false] Boolean

Causes promise to be rejected with an Error if no rows were updated.

[transacting] Transaction

Optionally run the query in a transaction.

Returns
Promise

A promise resolving to number of rows updated.

The updatePivot method is used exclusively on belongsToMany relations, and allows for updating pivot rows on the joining table.

This method (along with Collection#attach and Collection#detach) are mixed in to a Collection when returned by a belongsToMany relation.

collection.where(conditions) → Collection
source
Example
collection
  .where('favorite_color', '<>', 'green')
  .fetch()
  .then(results => {
    // ...
  })

// or

collection
  .where('favorite_color', 'red')
  .fetch()
  .then(results => {
    // ...
  })

collection
  .where({favorite_color: 'red', shoe_size: 12})
  .fetch()
  .then(results => {
    // ...
  })
Parameters
conditions Object|string

Either key, [operator], value syntax, or a hash of attributes to match. Note that these must be formatted as they are in the database, not how they are stored after Model#parse.

See
Collection#query
Returns
Collection

Self, this method is chainable.

This is used as convenience for the most common query method: adding a WHERE clause to the builder. Any additional knex methods may be accessed using query.

Accepts either key, value syntax, or a hash of attributes to constrain the results.

collection.withPivot(columns) → Collection
source
Parameters
columns string[]

Names of columns to be included when retrieving pivot table rows.

Returns
Collection

Self, this method is chainable.

The withPivot method is used exclusively on belongsToMany relations, and allows for additional fields to be pulled from the joining table.

var Tag = bookshelf.model('Tag', {
  comments: function() {
    return this.belongsToMany(Comment).withPivot(['created_at', 'order']);
  }
});
LODASH METHODS
countBy()
every()
filter()
find()
forEach()
groupBy()
includes()
invokeMap()
isEmpty()
map()
reduce()
reduceRight()
reject()
some()
sortBy()
toArray()
TYPE DEFINITIONS
reduceThenIterator(acumulator, model, index, length)
source
Parameters
acumulator mixed
model Model

The current model being iterated over.

index Number
length Number

Total number of models being iterated over.

This iterator is used by the reduceThen method to ietrate over all models in the collection.

EVENTS
collection.on("fetched", (collection, response, options) =>
source
Parameters
collection Collection

The collection performing the Collection#fetch.

response Object

Knex query response.

options Object

Options object passed to fetch.

Tutorials
Events
Returns
Promise

Fired after a fetch operation. A promise may be returned from the event handler for async behaviour.

Collection.EmptyError
CONSTRUCTION
new Collection.EmptyError()
source

Thrown by default when no records are found by fetch or Collection#fetchOne. This behavior can be overrided with the Model#requireFetch option.

Events
CONSTRUCTION
new Events()
source

Base Event class inherited by Model and Collection. It's not meant to be used directly, and is only displayed here for completeness.

METHODS
events.off(nameOrNames, callback)
source
Parameters
nameOrNames string

The name of the event or space separated list of events to stop listening to.

callback function

That callback to remove.

Remove a previously-bound callback event listener from an object. If no event name is specified, callbacks for all events will be removed.

events.on(nameOrNames, callback) → mixed
source
Parameters
nameOrNames string

The name or space separated names of events to register a callback for.

callback function

That callback to invoke whenever the event is fired.

Returns
mixed

The object where this is called on is returned to allow chaining this method call.

Registers an event listener. The callback will be invoked whenever the event is fired. The event string may also be a space-delimited list of several event names.

events.once(nameOrNames, callback)
source
Parameters
nameOrNames string

The name of the event or space separated list of events to register a callback for.

callback function

That callback to invoke only once when the event is fired.

Just like Events#on, but causes the bound callback to fire only once before being removed. Handy for saying "the next time that X happens, do this". When multiple events are passed in using the space separated syntax, the event will fire once for every event you passed in, not once for a combination of all events.

events.trigger(nameOrNames, […args])
source
Parameters
nameOrNames string

The name of the event to trigger. Also accepts a space separated list of event names.

[…args] mixed

Extra arguments to pass to the event listener callback function.

Trigger callbacks for the given event, or space-delimited list of events. Subsequent arguments to trigger will be passed along to the event callback.

events.triggerThen(name, […args]) → Promise
source
Parameters
name string

The event name or a whitespace-separated list of event names to be triggered.

[…args] mixed

Arguments to be passed to any registered event handlers.

Returns
Promise

A promise resolving to the return values of any triggered handlers.

A promise version of Events#trigger, returning a promise which resolves with all return values from triggered event handlers. If any of the event handlers throw an Error or return a rejected promise, the promise will be rejected. Used internally on the "creating", "updating", "saving", and "destroying" events, and can be helpful when needing async event handlers (e.g. for validations).

DOCUMENTATION GENERATED BY JSDOC 3.6.3 ON JUNE 7, 2020
