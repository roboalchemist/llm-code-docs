# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-execute/example-of-execute-step.md

# Example of Execute step

This example demonstrates the use of the **Execute for every row of input** option.

There is an incoming row with a **String** field called "first\_name" and an **Integer** field called "age":

| first\_name | age |
| ----------- | --- |
| Roger       | 26  |
| Peter       | 53  |

If the

`db.people.insertOne( { first: "?{first_name}", age: ?{age} } );`

command is in the **Script** area, once the transformation is executed and the two rows are input to the step, the following two commands will be evaluated with the wild card substitution and executed:

`db.people.insertOne( { first: "Roger", age: 26 } );`

`db.people.insertOne( { first: "Peter", age: 53 } );`
