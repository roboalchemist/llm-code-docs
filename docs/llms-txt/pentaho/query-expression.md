# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/examples/query-expression.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/examples/query-expression.md

# Query expression

MongoDB allows you to select and filter documents in a collection using specific fields and values. The [MongoDB Extended JSON](http://docs.mongodb.org/manual/reference/mongodb-extended-json/)documentation details how to use queries. Pentaho supports only the features discussed on this page.

The following table displays some examples of the syntax and structure of the queries you can use to request data from MongoDB:

| Query expression                                                     | Description                                                                                                                |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `{ name : "MongoDB" }`                                               | Queries all values where the name field has a value equal to MongoDB.                                                      |
| `{ name : { '$regex' : "m.*", '$options' : "i" } }`                  | Uses a regular expression to find name fields starting with `m`, case insensitive.                                         |
| `{ name : ﻿{ '$gt' : "M" ﻿} }`                                       | Searches all strings greater than `M`.                                                                                     |
| `{ name : { '$lte' : "T" } }`                                        | Searches all strings less than or equal to `T`.                                                                            |
| `{ name : { '$in' : ﻿[ "MongoDB", "MySQL" ] } }`                     | Finds all names that are either MongoDB or MySQL ([Reference](https://docs.mongodb.com/manual/reference/operator/query/)). |
| `{ name : { '$nin' : ﻿[ "MongoDB", "MySQL" ] } }`                    | Finds all names that are not either MongoDB or MySQL, or where the field is not set .                                      |
| `{ created_at : { $gte : { $date : "2014-12-31T00:00:00.000Z" } } }` | Finds all created\_at documents that are greater than or equal to the specified UTC date.                                  |
| `{ $where : "this.count == 1" }`                                     | Uses JavaScript to evaluate a condition.                                                                                   |
| `{ $query: {}, $orderby: { age : -1 } }`                             | Returns all documents in the collection named `collection` sorted by the age field in descending order.                    |
