# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/examples/aggregate-pipeline.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/examples/aggregate-pipeline.md

# Aggregate pipeline

MongoDB allows you to select and filter documents using the aggregation pipeline framework. The [Aggregation](http://docs.mongodb.org/manual/tutorial/aggregation-examples/) page in the MongoDB documentation provides additional examples of function calls.

The following table displays some examples of the query syntax and structure you can use to request data from MongoDB:

| Query expression                                                                                                                                     | Description                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ﻿`{ $match : {state : "FL", city : "ORLANDO" } }, {$sort : {pop : -1 } }`                                                                            | Returns all fields from all documents where the state field has a value of `FL` and the city field has a value of `ORLANDO`. The returned documents will be sorted by the pop field in descending order. |
| `{ $group : { _id: "$state"} }, { $sort : { _id : 1 } }`                                                                                             | Returns one field named `_id` containing the distinct values for state in ascending order. This is similar to the SQL statement `SELECT DISTINCT state AS _id FROM collection ORDER BY state ASC`.       |
| `{ $match : {state : "FL" } }, { $group: {_id: "$city" , pop: { $sum: "$pop" } } }, { $sort: { pop: -1 } }, { $project: {_id : 0, city : "$_id" } }` | Returns all documents where the state field has a value of `FL`, aggregates all values of pop for each city, sorts by population descending, and returns one field named city.                           |
| `{ $unwind : "$result" }`                                                                                                                            | Peels off the elements of an array individually, and returns one document for each element of the array.                                                                                                 |
