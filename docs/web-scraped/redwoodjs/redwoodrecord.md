# Source: https://docs.redwoodjs.com/docs/redwoodrecord

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [RedwoodRecord]

[Version: 8.8]

On this page

<div>

# RedwoodRecord

</div>

> RedwoodRecord is currently considered to be **Experimental**. We are hoping folks will start using it and give us feedback to help shape its development and developer experience.

RedwoodRecord is an ORM ([Object-relational Mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)) built on top of Prisma. It may be extended in the future to wrap other database-access packages.

RedwoodRecord is heavily inspired by [ActiveRecord](https://guides.rubyonrails.org/active_record_basics.html) which ships with [Ruby on Rails](https://rubyonrails.org). It presents a natural interface to the underlying data in your database, without worry about the particulars of SQL syntax.

## Background and Terminology[​](#background-and-terminology "Direct link to Background and Terminology") 

Before you can use RedwoodRecord you need to create classes for each database table you intend to access. Let\'s say we have a blog with three database tables:

``` 
┌───────────┐       ┌────────────┐      ┌────────────┐
│   User    │       │    Post    │      │  Comment   │
├───────────┤       ├────────────┤      ├────────────┤
│ id        │•──┐   │ id         │•──┐  │ id         │
│ name      │   └──<│ userId     │   └─<│ postId     │
│ email     │       │ title      │      │ name       │
└───────────┘       │ body       │      │ message    │
                    └────────────┘      └────────────┘
```

In database-speak we say that these tables have *one-to-many* relationships between them when moving from left to right in the diagram above: one User can have many Posts associated to it, and a Post can have many Comments. The \"one\" is denoted with a `•` on the arrow above and a `<` denotes the \"many.\"

You can leave it at that, as saying one-to-many explains both sides of the relationship, but it\'s sometimes convenient to refer to the relation in the \"opposite\" direction. Reading the diagram from right to left we could say that a comment *belongs to* a post (it has a foreign key `postId` that points to Post via `Comment.postId` → `Post.id`) and a Post belongs to a User (`Post.userId` → `User.id`)

There are also *many-to-many* relationships, such as a Product and Category---a Product can have many different Categories, and a Category will have many different Products connected to it:

``` 
┌───────────┐       ┌────────────┐
│  Product  │       │  Category  │
├───────────┤       ├────────────┤
│ id        │>─────<│ id         │
│ name      │       │ name       │
│ upc       │       │ shelf      │
└───────────┘       └────────────┘
```

These tables don\'t have any foreign keys (`productId` or `categoryId`) so how do they keep track of each other? Generally you\'ll create a *join table* between the two that references each other\'s foreign key:

``` 
┌───────────┐      ┌───────────────────┐       ┌────────────┐
│  Product  │      │  ProductCategory  │       │  Category  │
├───────────┤      ├───────────────────┤       ├────────────┤
│ id        │•────<│ productId         │   ┌──•│ id         │
│ name      │      │ categoryId        │>──┘   │ name       │
│ upc       │      └───────────────────┘       │ shelf      │
└───────────┘                                  └────────────┘
```

Now we\'re back to one-to-many relationships. In Prisma this join table is created and maintained for you. It will be named `_CategoryToPost` and the foreign keys will simply be named `A` and `B` and point to the two separate tables. Prisma refers to this as an [implicit many-to-many](https://www.prisma.io/docs/concepts/components/prisma-schema/relations/many-to-many-relations#implicit-many-to-many-relations) relationship.

If you want to create the join table yourself and potentially store additional data there (like a timestamp of when the product was categorized) then this is simply a one-to-many relationship on both sides: a Product has many ProductCategories and a Category has many ProductCategories. Prisma refers to this as an [explicitly many-to-many](https://www.prisma.io/docs/concepts/components/prisma-schema/relations/many-to-many-relations#explicit-many-to-many-relations) relationship.

> TODO: We\'ll be adding logic soon that will let you get to the categories from a product record (and vice versa) in explicit many-to-manys without having to manually go through ProductCategory. From this:
>
> ::: 
> ::: codeBlockContent_QJqH
> ``` 
> const product = await Product.find(1)
> const productCategories = await product.productCategories.all()
> const categories = productCategories.map(async (pc) => await pc.categories.all()).flat()
> ```
> :::
> :::
>
> To this:
>
> ::: 
> ::: codeBlockContent_QJqH
> ``` 
> const product = await Product.find(1)
> const categories = await product.categories.all()
> ```
> :::
> :::

The only other terminology to keep in mind are the terms *model* and *record*. A *model* is the name for the class that represents one database table. The example above has three models: User, Post and Comment. Prisma also calls each database-table declaration in their `schema.prisma` declaration file a \"model\", but when we refer to a \"model\" in this doc it will mean the class that extends `RedwoodRecord`. A *record* is a single instance of our model that now represents a single row of data in the database.

So: I use the User model to find a given user in the database, and, assuming they are found, I now have a single user record (an instance of the User model).

## Usage[​](#usage "Direct link to Usage") 

You\'ll want to add RedwoodRecord\'s package to the api side:

``` 
yarn workspace api add @redwoodjs/record
```

First you\'ll need to create a model to represent the database table you want to access. In our blog example, let\'s create a User model:

api/src/models/User.js

``` 
import  from '@redwoodjs/record'

export default class User extends RedwoodRecord 
```

Now we need to parse the Prisma schema, store it as a cached JSON file, and create an `index.js` file with a couple of config settings:

``` 
yarn rw record init
```

You\'ll see that this created `api/src/models/datamodel.js` and `api/src/models/index.js`.

Believe it or not, that\'s enough to get started! Let\'s try using the Redwood console to make some quick queries without worrying about starting up any servers:

> TODO: Models don\'t quite work correctly in the console. The require and fetching of records below will work, but actually trying to read any properties returns `undefined`. For now you\'ll need to test out RedwoodRecord directly in your app.

``` 
yarn rw c
```

Now we\'ve got a standard Node REPL but with a bunch of Redwood goodness loaded up for us already. First, let\'s require our model:

``` 
const  = require('./api/src/models')
```

And now we can start querying and modifying our data:

``` 
await User.all()
const newUser = await User.create()
newUser.name = 'Robert'
await newUser.save()
await User.find(1)
await User.findBy()
await newUser.destroy()
```

### Initializing New Records[​](#initializing-new-records "Direct link to Initializing New Records") 

To create a new record in memory only (not yet saved to the database) use `build()`:

``` 
const user = User.build()
```

Note that `build` simply builds the record in memory, and thus is not asynchronous, whereas other model methods that interact with Prisma/the DB are.

See [create/save](#save) below for saving this record to the database.

### Errors[​](#errors "Direct link to Errors") 

When a record cannot be saved to the database, either because of database errors or [validation](#validation) errors, the `errors` property will be populated with the error message(s).

``` 
const user = User.build()
await user.save() // => false
user.hasError() // => true
user.errors // => 
user.errors.email // => ['must not be null']
```

> `base` is a special key in the errors object and is for errors that don\'t apply to a single attribute, like `email`. For example, if you try to delete a record that doesn\'t exist (maybe someone else deleted it between when you retrieved it from the database and when you tried to delete it) you\'ll get an error on the `base` attribute:
>
> `user.errors.base // => ['User record to destroy not found']`

You can preemptively check for errors before attempting to modify the record, but only for errors that would be caught with [validation](#validation), by using `isValid`:

``` 
const user = User.build()
user.isValid // => false
user.errors.email // => ['must be formatted like an email address']
```

### Validation[​](#validation "Direct link to Validation") 

Records can be checked for valid data before saving to the database by using the same [validation types](/docs/services#absence) available to [Service Validations](/docs/services#service-validations):

``` 
export default class User extends RedwoodRecord ,
    username:  },
  }
}

const user = User.build()
await user.save() // => false
user.errors.email = ['must be present']
user.errors.username = ['must be at least 2 characters']
user.email = 'rob@redwoodjs.com'
user.username = 'rob'
await user.save()
```

### Finding Records[​](#finding-records "Direct link to Finding Records") 

There are a few different ways to find records for a model. Sometimes you want to find multiple records (all that match certain criteria) and sometimes only one (the one record with a certain email address).

#### where()[​](#where "Direct link to where()") 

`where()` is for finding multiple records. It returns an array of model records. The first argument is the properties that you would normally set as the `where` value in Prisma\'s [`findMany()` function](https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#findmany). The second argument (optional) is any additional properties (like ordering or limiting) that you want to perform on the resulting records:

``` 
await User.where() // would return all records
await User.where()
await User.where(,  })
```

#### all()[​](#all "Direct link to all()") 

`all()` is simply a synonym for `where()` but makes it clearer that your intention is truly to select all records (and optionally sort/order them). The first (and only) argument is now the additional properties (like `sort` and `orderBy`):

``` 
await User.all()
await User.all( })
```

#### find()[​](#find "Direct link to find()") 

Finds a single record by that record\'s primary key. By default that is `id` but you can change the primary key of a model by defining it in the class definition:

``` 
export default class User extends RecordRecord 
```

This call will throw an error if the record is not found: if you are trying to select a user by ID, presumably you expect that user to exist. So, it not existing is an exceptional condition. Behind the scenes this uses Prisma\'s [`findFirst()` function](https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#findfirst).

``` 
await User.find(123)
```

#### findBy()[​](#findby "Direct link to findBy()") 

Finds a single record by certain criteria. Similar to `where()`, but will only return the first record that matches. The first argument is the properties that you would normally set as the `where` value to Prisma\'s [`findFirst()` function](https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#findmany). The second argument (optional) is any additional properties (like ordering or limiting) that you want to perform on the resulting records before selecting one:

``` 
await User.findBy()
await User.findBy( } }, , take: 10 })
```

If no record matching your query was found, it returns `null`.

#### first()[​](#first "Direct link to first()") 

Alias for `findBy()`. This function can be used in your code to show your intention to only use the first of potentially multiple records that could match with `findBy()`.

``` 
const randomCoreMember = await User.first( } })
```

### Creating Records[​](#creating-records "Direct link to Creating Records") 

You can create new records with your RedwoodRecord model in two ways:

#### create()[​](#create "Direct link to create()") 

Initializes a new record and saves it. If the save fails, `create` will return `false` instead of the instance of your record. If you need your new model instance (even on a failed save) use the `build()` version next.

The first argument is the data that would be given to Prisma\'s `create()` function. The (optional) second argument are any additional properties that are passed on to Prisma:

``` 
await User.create()
await User.create(
  ,
  
)
```

#### save()[​](#save "Direct link to save()") 

When calling `save()` on a record that hasn\'t been saved to the database, a new record will be created. If the record cannot be saved this call will return `false`. You can have it throw an error instead by including `` in the first argument.

If the record cannot be saved you can inspect it for errors.

``` 
const user = User.build()
await user.save()
// or
await user.save()
// check for errors
user.hasErrors // => true
user.errors.email // => ['can't be null']
```

### Updating Records[​](#updating-records "Direct link to Updating Records") 

There are two ways to update a record. You can either 1) list all of the attributes to change in a call to `update()`, or 2) set the attributes manually and then call `save()`.

#### update()[​](#update "Direct link to update()") 

Call `update()` on a record, including the attributes to change as the first argument. The second (optional) argument are any properties to forward to Prisma on updating. Returns `false` if the record did not save, otherwise returns itself with the newly saves attributes.

``` 
const user = await User.find(123)
await user.update()
// or
await user.update(, )
```

#### save()[​](#save-1 "Direct link to save()") 

Save changes made to a record. The first (optional) argument includes any properties to be forwarded to Prisma, as well as the option to throw an error on a failed save:

``` 
const user = await User.find(123)
user.email = 'rob.cameron@redwoodjs.com'
await user.save()
// or
await user.save()
```

### Deleting Records[​](#deleting-records "Direct link to Deleting Records") 

Records can be deleted easily enough. Coming soon will be class functions for deleting one or multiple records, without having to instantiate an instance of the model first.

#### destroy()[​](#destroy "Direct link to destroy()") 

Call on a record to delete it in the database. The first (optional) argument are any properties to forward to Prisma when deleting, as well as the option to throw an error if the delete fails. This function returns `false` if the record could not be deleted, otherwise returns the record itself.

``` 
const user = await User.find(123)
await user.destroy()
// or
await user.destroy()
```

### Relationships[​](#relationships "Direct link to Relationships") 

As shown in [Background and Terminology](#background-and-terminology) above, RedwoodRecord provides a way to get data from related models. For example, to get the posts belonging to a user via what we call a *relation proxy*:

``` 
const user = await User.find(123)
const posts = await user.posts.all()
```

In this example `posts` is the proxy. All of the normal finder methods available on a model (`where()`, `all()`, `find()` and `findBy()`) are all available to be called on the relation proxy. But that\'s not all: you can create records as well and they will automatically be associated to the parent record:

``` 
const user = await User.find(123)
const post = await user.posts.create()
post.userId // => 123
```

#### One-to-many[​](#one-to-many "Direct link to One-to-many") 

The *many* records are accessible through the relation proxy:

``` 
const user = await User.find(123)
const post = await user.posts.first()
const comments = await post.comments.all()
```

You can also create a record:

``` 
const user = await User.find(123)
const post = await user.posts.create()
```

#### Belongs-to[​](#belongs-to "Direct link to Belongs-to") 

A belongs-to relationship implies that you have the child record and want the parent. In a belongs-to relationship there is only ever a single parent, so there is no need for a relationship proxy property: there is only one record that will ever be returned.

``` 
const post = await Post.first()
const user = await post.user
```

> You cannot currently create a belongs-to record through the parent, but we\'re working on syntax to enable this!

#### Many-to-many[​](#many-to-many "Direct link to Many-to-many") 

If you have an implicit many-to-many relationship then you will access the records similar to the one-to-many type:

``` 
const product = await Product.find(123)
const categories = await product.categories.all()
```

If you have an explicit many-to-many relationship then you need to treat it as a two-step request. First, get the one-to-many relationships for the join table, then a belongs-to relationship for the data you actually want:

``` 
Product -> one-to-many -> ProductCategories -> belongs-to -> Category
-------                   -----------------                  --------
```

``` 
const product = await Product.find(123)
const productCategories = await product.productCategories.all()
const categories = await Promise.all(
  productCategories.map(async (pc) => await pc.category)
)
```

If you wanted to create a new record this way, you would need to create the join table record after having already created/retrieved the records on either side of the relation:

``` 
const product = await Product.find(123)
const category = await Category.find(234)
await ProductCategory.create()
```

> We\'re working on improving this syntax to make interacting with these records as simple as the implicit version. Stay tuned!

## Coming Soon[​](#coming-soon "Direct link to Coming Soon") 

The following features are in development but are not available in this experimental release.

### Lifecycle Callbacks[​](#lifecycle-callbacks "Direct link to Lifecycle Callbacks") 

Coming soon will be the ability create functions around the lifecycle of a record. For example, to set a newly-created user\'s default preferences, you may want an `afterCreate` callback that invokes a function (syntax not final):

``` 
export default class User extends RedwoodRecord )
  }
}
```

Or make sure that a user has transferred ownership of some data before closing their account:

``` 
export default class User extends RedwoodRecord 
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/redwoodrecord.md)