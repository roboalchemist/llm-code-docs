# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-execute/commands-execute-step.md

# Execute commands

The commands are divided into two sub-types. Those that operate directly on the selected database, and those that operate on a collection of the selected database. For more information, see:

* [Database commands](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-execute/commands-execute-step/database-commands)
* [Collection commands](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-execute/commands-execute-step/collection-commands)

Generally the commands follow the structure of commands in the MongoDB shell. However, there are some cases where extra input and output options are limited. Commands may accept arguments of

* STRING (double or single qoutes)
* BSON (less restrictive JSON)
* \[ BSON, ...] (a collection of BSON).
